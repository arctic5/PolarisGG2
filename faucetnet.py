from ctypes import *

global faucetnet
faucetnet = cdll.LoadLibrary("faucetNetworking.dll")

def buffer_create():
    return c_double(faucetnet.buffer_create())
def tcp_listen(port):
    return c_double(faucetnet.tcp_listen(port))
def socket_has_error(handle):
    return c_double(faucetnet.socket_has_error(handle))
def socket_error(handle):
    return c_char_p(faucetnet.socket_error(handle))
def tcp_connect(ip, port):
    return c_double(faucetnet.tcp_connect(ip, port))
def write_ubyte(handle, value):
    return c_double(faucetnet.write_ubyte(handle, value))
def write_ushort(handle, value):
    return c_double(faucetnet.write_ushort(handle, value))
def write_string(handle, value):
    return c_double(faucetnet.write_string(handle, value))
def writeKeyValue(handle, key, value):
    if(len(key) > 255):
        print "ERROR: KEY TOO LONG"
    if(len(value) > 65535):
        value = value[:65535]
    write_ubyte(handle, string_length(key))
    write_string(handle, key)
    write_ushort(handle, string_length(value))
    write_string(handle, value)
    return 0