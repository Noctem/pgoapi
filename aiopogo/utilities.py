from time import time
from json import JSONEncoder
from struct import pack, unpack

def f2i(float_val):
    return unpack('<q', pack('<d', float_val))[0]


def to_camel_case(string):
    return ''.join(word.capitalize() for word in string.split('_'))


# JSON Encoder to handle bytes
class JSONByteEncoder(JSONEncoder):
    def default(self, o):
        return o.decode('ascii')


def get_time_ms():
    return int(time() * 1000)


class IdGenerator:
    '''New C++ based generator'''

    def __init__(self):
        self.high = 1
        self.request = 1

    def next(self):
        #         self.rpcIdHigh = (Math.pow(7, 5) * self.rpcIdHigh) % (Math.pow(2, 31) - 1);
        self.high = (7**5 * self.high) % ((2**31)-1)
        return self.high

    def request_id(self):
        self.request += 1
        return (self.next() << 32) | self.request
