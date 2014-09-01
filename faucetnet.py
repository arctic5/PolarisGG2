from ctypes import *

global faucetnet
faucetnet = cdll.LoadLibrary("faucetNetworking.dll")

def dllStartup():
    return c_double(faucetnet.dllStartup())
dllStartup()
def buffer_create():
    return c_double(faucetnet.buffer_create())
    
def tcp_listen(port):
    return faucetnet.tcp_listen(port)
    
def socket_has_error(handle):
    return c_double(faucetnet.socket_has_error(handle))
    
def socket_error(handle):
    faucetnet.socket_error.restype = c_char_p
    return faucetnet.socket_error(handle)

def tcp_connect(ip, port):
    return c_double(faucetnet.tcp_connect(ip, port))
    
def write_ubyte(handle, value):
    return c_double(faucetnet.write_ubyte(handle, value))
    
def write_ushort(handle, value):
    return c_double(faucetnet.write_ushort(handle, value))
    
def write_string(handle, value):
    return c_double(faucetnet.write_string(handle, value))
    
def udp_send(handle, host, port):
    return c_double(faucetnet.udp_send(handle, host, port))
    
def set_little_endian(handle, littleEndian):
    return c_double(faucetnet.set_little_endian(handle, littleEndian))
    
def write_buffer(destHandle, bufferHandle):
    return c_double(faucetnet.write_buffer(destHandle, bufferHandle))
def buffer_destroy(bufferHandle):
    return c_double(faucetnet.buffer_destroy(bufferHandle))
    
    
    
    
def writeKeyValue(handle, key, value):
    if(len(key) > 255):
        print "ERROR: KEY TOO LONG"
    if(len(value) > 65535):
        value = value[:65535]
    write_ubyte(handle, len(key))
    write_string(handle, key)
    write_ushort(handle, len(value))
    write_string(handle, value)
    return 0
    
def parseUuid(uuidString, buffer):
    uuidString = uuidString.lower()
    uuidString = uuidString.replace("-", "", 4)
    #print uuidString
    
    if(len(uuidString) != 32):
        print "INVALID UUID1"
        
    posValueString = "0123456789abcdef"
    
    for i in range(0,16):
        currentNibble = uuidString[i*2+1]
        if(posValueString.find(currentNibble) == 0):
            print "INVALID UUID2"
        numericByte = (posValueString.find(posValueString)-1)*16
        
        currentNibble = uuidString[i*2+2]
        if(posValueString.find(currentNibble) == 0):
            print "INVALID UUID3"
        numericByte += posValueString.find(posValueString)-1
        
        write_ubyte(buffer, numericByte)
        return 0