from logging import getLogger

from yarl import URL
from aiohttp import BasicAuth
try:
    from aiosocks import Socks4Auth, Socks5Auth
except ImportError:
    class Socks4Auth(Exception):
        def __init__(*args, **kwargs):
            raise ImportError(
                'You must install aiosocks to use a SOCKS proxy.')
    Socks5Auth = Socks4Auth

from . import __title__, __version__
from .rpc_api import RpcApi, RpcState
from .auth_ptc import AuthPtc
from .auth_google import AuthGoogle
from .hash_server import HashServer
from .exceptions import AuthTokenExpiredException, InvalidCredentialsException, NoPlayerPositionSetException, ServerApiEndpointRedirectException
from .pogoprotos.networking.requests.request_type_pb2 import RequestType


class PGoApi:
    log = getLogger(__name__)
    log.info('%s v%s', __title__, __version__)

    def __init__(self, lat=None, lon=None, alt=None, proxy=None, device_info=None):
        self.auth_provider = None
        self.state = RpcState()

        self._api_endpoint = 'https://pgorelease.nianticlabs.com/plfe/rpc'

        self.latitude = lat
        self.longitude = lon
        self.altitude = alt

        self.proxy_auth = None
        self.proxy = proxy
        self.device_info = device_info

    async def set_authentication(self, provider='ptc', username=None, password=None, timeout=10, locale='en_US', refresh_token=None):
        if provider == 'ptc':
            self.auth_provider = AuthPtc(
                username,
                password,
                proxy=self._proxy,
                proxy_auth=self.proxy_auth,
                timeout=timeout)
        elif provider == 'google':
            self.auth_provider = AuthGoogle(
                proxy=self._proxy, refresh_token=refresh_token)
            if refresh_token:
                return await self.auth_provider.get_access_token()
        else:
            raise InvalidCredentialsException(
                "Invalid authentication provider - only ptc/google available.")

        await self.auth_provider.user_login(username, password)

    def set_position(self, lat, lon, alt=None):
        self.log.debug('Set Position - Lat: %s Lon: %s Alt: %s', lat, lon, alt)
        self.latitude = lat
        self.longitude = lon
        self.altitude = alt

    def create_request(self):
        return PGoApiRequest(self)

    @staticmethod
    def activate_hash_server(hash_token, conn_limit=300, go_hash=False):
        HashServer.set_token(hash_token)
        HashServer.activate_session(conn_limit, go_hash)

    @property
    def position(self):
        return self.latitude, self.longitude, self.altitude

    @property
    def api_endpoint(self):
        return self._api_endpoint

    @api_endpoint.setter
    def api_endpoint(self, api_url):
        if api_url.startswith("https"):
            self._api_endpoint = URL(api_url)
        else:
            self._api_endpoint = URL('https://' + api_url + '/rpc')

    @property
    def proxy(self):
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        if proxy is None:
            self._proxy = proxy
        else:
            self._proxy = URL(proxy)
            if self._proxy.user:
                scheme = self._proxy.scheme
                if scheme == 'http':
                    self.proxy_auth = BasicAuth(
                        self._proxy.user, self._proxy.password)
                elif scheme == 'socks5':
                    self.proxy_auth = Socks5Auth(
                        self._proxy.user, self._proxy.password)
                elif scheme == 'socks4':
                    self.proxy_auth = Socks4Auth(self._proxy.user)
                else:
                    raise ValueError(
                        'Proxy protocol must be http, socks5, or socks4.')

    @property
    def start_time(self):
        return self.state.start_time

    def __getattr__(self, func):
        async def function(**kwargs):
            request = self.create_request()
            getattr(request, func)(**kwargs)
            return await request.call()

        if func.upper() in RequestType.keys():
            return function
        else:
            raise AttributeError('{} not known.'.format(func))


class PGoApiRequest:
    log = getLogger(__name__)

    def __init__(self, parent):
        self.__parent__ = parent
        self._req_method_list = []

    async def call(self):
        parent = self.__parent__
        auth_provider = parent.auth_provider
        position = parent.position
        try:
            assert position[0] is not None and position[1] is not None
        except AssertionError:
            raise NoPlayerPositionSetException('No position set.')

        request = RpcApi(auth_provider, parent.state)
        while True:
            try:
                response = await request.request(parent.api_endpoint, self._req_method_list, position, parent.device_info, parent._proxy, parent.proxy_auth)
                break
            except AuthTokenExpiredException:
                self.log.info('Access token rejected! Requesting new one...')
                await auth_provider.get_access_token(force_refresh=True)
            except ServerApiEndpointRedirectException as e:
                self.log.debug('API endpoint redirect... re-executing call')
                parent.api_endpoint = e.endpoint

        # cleanup after call execution
        self._req_method_list = []

        return response

    def list_curr_methods(self):
        for i in self._req_method_list:
            print("{} ({})".format(RequestType.Name(i), i))

    def __getattr__(self, func):
        func = func.upper()

        def function(**kwargs):
            self.log.debug('Creating a new request...')

            try:
                if kwargs:
                    self._req_method_list.append(
                        (RequestType.Value(func), kwargs))
                    self.log.debug("Arguments of '%s': \n\r%s", func, kwargs)
                else:
                    self._req_method_list.append(RequestType.Value(func))
                    self.log.debug("Adding '%s' to RPC request", func)
            except ValueError:
                raise AttributeError('{} not known.'.format(func))

            return self

        return function
