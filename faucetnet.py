from ctypes import *

class FaucetNet:
    def __init__(self):
        try:
            self._dll = CDLL("faucetNetworking.dll")
        except:
            print "shit"
    def bind_function(self, funcname, args=None, returns=None):
        func = getattr(self._dll, funcname, None)
        return func
        
fct = FaucetNet()
_bind = fct.bind_function

dllStartup = _bind("dllStartup", None, c_double)
buffer_create = _bind("dllStartup", None, c_int)
tcp_listen = _bind("tcp_listen", c_double, c_double)

    
# def tcp_listen(port):
    # return faucetnet.tcp_listen(port)

# def tcp_connect(ip, port):
    # return c_double(faucetnet.tcp_connect(ip, port))
    
# def socket_has_error(handle):
    # return faucetnet.socket_has_error(handle)
    
# def socket_error(handle):
    # faucetnet.socket_error.restype = c_char_p
    # return faucetnet.socket_error(handle)

# def socket_remote_ip(handle):
    # faucetnet.socket_remote_ip.restype = c_char_p
    # return faucetnet.socket_remote_ip(handle)
    
# def socket_accept(handle):
    # faucetnet.socket_accept.restype = c_double
    # return faucetnet.socket_accept(handle)
    
# def socket_send(handle):
    # return c_double(faucetnet.socket_send(handle))

# def socket_receivebuffer_size(handle):
    # return c_double(faucetnet.socket_receivebuffer_size(handle))
# def socket_destroy(handle):
    # return c_double(faucetnet.socket_destroy(handle))
    
# def write_ubyte(handle, value):
    # return c_double(faucetnet.write_ubyte(handle, value))
    
# def write_ushort(handle, value):
    # return c_double(faucetnet.write_ushort(handle, value))
    
# def write_string(handle, value):
    # return c_double(faucetnet.write_string(handle, value))
    
# def write_buffer(destHandle, bufferHandle):
    # return c_double(faucetnet.write_buffer(destHandle, bufferHandle))
    
# def buffer_destroy(bufferHandle):
    # #faucetnet.buffer_destroy.argtype = c_double
    # return c_double(faucetnet.buffer_destroy(bufferHandle)).value
    
# def udp_send(handle, host, port):
    # return c_double(faucetnet.udp_send(handle, host, port))
    
# def set_little_endian(handle, littleEndian):
    # return c_double(faucetnet.set_little_endian(handle, littleEndian))
    
    
    
    
    
# def writeKeyValue(handle, key, value):
    # if(len(key) > 255):
        # print "ERROR: KEY TOO LONG"
    # if(len(value) > 65535):
        # value = value[:65535]
    # write_ubyte(handle, len(key))
    # write_string(handle, key)
    # write_ushort(handle, len(value))
    # write_string(handle, value)
    # return 0
    
# def parseUuid(uuidString, buffer):
    # uuidString = uuidString.lower()
    # uuidString = uuidString.replace("-", "", 4)
    # #print uuidString
    
    # if(len(uuidString) != 32):
        # print "INVALID UUID1"
        
    # posValueString = "0123456789abcdef"
    
    # for i in range(0,16):
        # currentNibble = uuidString[i*2+1]
        # if(posValueString.find(currentNibble) == 0):
            # print "INVALID UUID2"
        # numericByte = (posValueString.find(posValueString)-1)*16
        
        # currentNibble = uuidString[i*2+2]
        # if(posValueString.find(currentNibble) == 0):
            # print "INVALID UUID3"
        # numericByte += posValueString.find(posValueString)-1
        
        # write_ubyte(buffer, numericByte)
        # return 0