from ctypes import c_int32, c_int64
from base64 import b64encode
from asyncio import get_event_loop, TimeoutError, CancelledError, sleep
from itertools import cycle
from time import time
from logging import getLogger

from aiohttp import ClientSession, ClientError, ClientResponseError, ServerConnectionError, ServerTimeoutError

from . import json_dumps, json_loads
from .connector import TimedConnector
from .exceptions import BadHashRequestException, ExpiredHashKeyException, HashingOfflineException, HashingTimeoutException, MalformedHashResponseException, NoHashKeyException, TempHashingBanException, UnexpectedHashResponseException
from .utilities import f2i


class HashServer:
    _session = None
    multi = False
    goHash = False
    loop = get_event_loop()
    status = {}
    log = getLogger('hashing')
    endPointUrl = "http://pokehash.buddyauth.com/api/v137_1/hash"

    def __init__(self):
        try:
            self.instance_token = self.auth_token
        except AttributeError:
            NoHashKeyException(
                'You must provide a hash key before making a request.')

    async def hash(self, timestamp, latitude, longitude, accuracy, authticket, sessiondata, requests):
        status = self.key_status
        iteration = 0
        try:
            while status['remaining'] < 3 and time() < status['refresh']:
                if self.multi and iteration < self.multi:
                    self.instance_token = self.auth_token
                    status = self.key_status
                    iteration += 1
                else:
                    self.log.info('Out of hashes, waiting for new period.')
                    if not self.goHash:
                        await sleep(status['refresh'] - time() + 1, loop=self.loop)
                        break
                    # Go Hash doesn't have an expiry period so you would top up credit, we will try again in 5 seconds    
                    else: 
                        await sleep(5, loop=self.loop)
                        break
        except KeyError:
            pass
        
        headers = {'X-AuthToken': self.instance_token}       
        if self.goHash:
             # extra header ensures no more than 5000 hashes per minute when using Go Hash. You can up this if your CPU can handle it
             headers = {'X-AuthToken': self.instance_token, 'X-RateLimit':'5000'}
        payload = {
            'Timestamp': timestamp,
            'Latitude64': f2i(latitude),
            'Longitude64': f2i(longitude),
            'Accuracy64': f2i(accuracy),
            'AuthTicket': b64encode(authticket),
            'SessionData': b64encode(sessiondata),
            'Requests': [b64encode(x.SerializeToString()) for x in requests]
        }

        # request hashes from hashing server
        for attempt in range(3):
            try:
                async with self._session.post(self.endPointUrl, headers=headers, json=payload) as resp:
                    if resp.status == 400:
                        status['failures'] += 1

                        if status['failures'] < 10:
                            if attempt < 2:
                                await sleep(1.0)
                                continue
                            raise BadHashRequestException('400 was returned from the hashing server.')

                        if self.multi:
                            self.log.warning(
                                '{:.10}... expired, removing from rotation.'.format(
                                    self.instance_token))
                            self.remove_token(self.instance_token)
                            self.instance_token = self.auth_token
                            if attempt < 2:
                                headers = {'X-AuthToken': self.instance_token}
                                continue
                            return await self.hash(timestamp, latitude, longitude, accuracy, authticket, sessiondata, requests)
                        raise ExpiredHashKeyException("{:.10}... appears to have expired.".format(self.instance_token))

                    resp.raise_for_status()
                    status['failures'] = 0

                    response = await resp.json(encoding='ascii', loads=json_loads)
                    headers = resp.headers
                    break
            except ClientResponseError as e:
                if e.code == 403:
                    raise TempHashingBanException('Your IP was temporarily banned for sending too many requests with invalid keys')
                # allow for 429 from bossland AND for 430 from goHash
                elif e.code == 429 or e.code == 430:
                    status['remaining'] = 0
                    self.instance_token = self.auth_token
                    if e.code == 429:
                        if self.goHash:
                            self.log.warning("Error 429 - Artificial hash limit reached, consider a higher value for X-RateLimit header in Go Hash request.")
                        else:
                            self.log.warning("Error 429 - Out of hashes for this period.")
                    else:
                        self.log.warning("Error 430 - No credit remaining on the Go Hash key.")
                    return await self.hash(timestamp, latitude, longitude, accuracy, authticket, sessiondata, requests)
                elif e.code >= 500 or e.code == 404:
                    if e.code == 503 and self.goHash:
                        self.log.warning("Error 503 - Go Hash server cannot handle the load.")
                    if e.code == 549 or e.code == 550 and self.goHash:
                        self.log.warning("Error 549|550 something bad happened between Bossland and Go Hash not successful after multiple retries.")
                    raise HashingOfflineException(
                        'Hashing server error {}: {}'.format(
                            e.code, e.message))
                else:
                    raise UnexpectedHashResponseException('Unexpected hash code {}: {}'.format(e.code, e.message))
            except ValueError as e:
                raise MalformedHashResponseException('Unable to parse JSON from hash server.') from e
            except (TimeoutError, ServerConnectionError, ServerTimeoutError) as e:
                if attempt < 2:
                    self.log.info('Hashing request timed out.')
                    await sleep(1.5)
                else:
                    raise HashingTimeoutException('Hashing request timed out.') from e
            except ClientError as e:
                error = '{} during hashing. {}'.format(e.__class__.__name__, e)
                if attempt < 2:
                    self.log.info(error)
                else:
                    raise HashingOfflineException(error) from e

        try:
            status['remaining'] = int(headers['X-RateRequestsRemaining'])
            status['period'] = int(headers['X-RatePeriodEnd'])
            status['maximum'] = int(headers['X-MaxRequestCount'])
            status['expiration'] = int(headers['X-AuthTokenExpiration'])
            HashServer.status = status
        except (KeyError, TypeError, ValueError):
            pass

        try:
            return (c_int32(response['locationHash']).value,
                    c_int32(response['locationAuthHash']).value,
                    [c_int64(x).value for x in response['requestHashes']])
        except CancelledError:
            raise
        except Exception as e:
            raise MalformedHashResponseException('Unable to load values from hash response.') from e

    @property
    def _multi_token(self):
        return next(self._tokens)

    @property
    def _multi_status(self):
        return self.key_statuses[self.instance_token]

    @classmethod
    def activate_session(cls, conn_limit=300, go_hash=False):
        cls.goHash = go_hash
        if cls._session and not cls._session.closed:
            return
        if cls.goHash:
            cls.endPointUrl = "http://hash.goman.io/api/v137_1/hash"
            cls.log.warning("Hash server set to Go Hash mode. Please ensure you are using a Go Hash NOT a Bossland hash key.")
        else:
            cls.log.warning("Hash server set to Bossland mode. Please ensure you are using a Bossland NOT a Go Hash hash key.")
        conn = TimedConnector(loop=cls.loop,
                              limit=conn_limit,
                              verify_ssl=False)
        headers = (('Content-Type', 'application/json'),
                   ('Accept', 'application/json'),
                   ('User-Agent', 'Python aiopogo'))
        cls._session = ClientSession(connector=conn,
                                     loop=cls.loop,
                                     headers=headers,
                                     raise_for_status=False,
                                     conn_timeout=4.5,
                                     json_serialize=json_dumps)

    @classmethod
    def close_session(cls):
        if not cls._session or cls._session.closed:
            return
        cls._session.close()

    @classmethod
    def remove_token(cls, token):
        tokens = set(cls.key_statuses)
        tokens.discard(token)
        del cls.key_statuses[token]
        if len(tokens) > 1:
            cls.multi = len(tokens)
            cls._tokens = cycle(tokens)
        else:
            cls.multi = False
            cls.auth_token = tokens.pop()
            cls.key_status = cls.key_statuses[cls.auth_token]

    @classmethod
    def set_token(cls, token):
        if isinstance(token, (tuple, list, set, frozenset)) and len(token) > 1:
            cls._tokens = cycle(token)
            cls.auth_token = cls._multi_token
            cls.multi = len(token)
            cls.key_statuses = {t: {'failures': 0} for t in token}
            cls.key_status = cls._multi_status
        else:
            cls.auth_token = token
            cls.key_status = {'failures': 0}
            