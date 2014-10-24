from ctypes import *

fct = CDLL("Faucet Networking.dll")

fct.dllStartup()

buffer_create = fct.buffer_create
buffer_create.restype = c_double

write_ubyte = fct.write_ubyte
write_ubyte.argtypes = [c_double, c_double]
write_ubyte.restype = c_double

write_byte = fct.write_byte
write_byte.argtypes = [c_double, c_double]
write_byte.restype = c_double

write_ushort = fct.write_ushort
write_ushort.argtypes = [c_double, c_double]
write_ushort.restype = c_double

write_short = fct.write_short
write_short.argtypes = [c_double, c_double]
write_short.restype = c_double

write_uint = fct.write_uint
write_uint.argtypes = [c_double, c_double]
write_uint.restype = c_double

write_int = fct.write_int
write_int.argtypes = [c_double, c_double]
write_int.restype = c_double

write_float = fct.write_float
write_float.argtypes = [c_double, c_double]
write_float.restype = c_double

write_double = fct.write_double
write_double.argtypes = [c_double, c_double]
write_double.restype = c_double

write_string = fct.write_string
write_string.argtypes = [c_double, c_char_p]
write_string.restype = c_double

read_ubyte = fct.read_ubyte
read_ubyte.argtypes = [c_double]
read_ubyte.restype = c_double

read_byte = fct.read_byte
read_byte.argtypes = [c_double]
read_byte.restype = c_double

read_ushort = fct.read_ushort
read_ushort.argtypes = [c_double]
read_ushort.restype = c_double

read_short = fct.read_short
read_short.argtypes = [c_double]
read_short.restype = c_double

read_uint = fct.read_uint
read_uint.argtypes = [c_double]
read_uint.restype = c_double

read_int = fct.read_int
read_int.argtypes = [c_double]
read_int.restype = c_double

read_float = fct.read_float
read_float.argtypes = [c_double]
read_float.restype = c_double

read_double = fct.read_double
read_double.argtypes = [c_double]
read_double.restype = c_double

read_string = fct.read_string
read_string.argtypes = [c_double]
read_string.restype = c_char_p

tcp_listen = fct.tcp_listen
tcp_listen.argtypes = [c_double]
tcp_listen.restype = c_double

socket_has_error = fct.socket_has_error
socket_has_error.argtypes = [c_double]
socket_has_error.restype = c_double

socket_accept = fct.socket_accept
socket_accept.argtypes = [c_double]
socket_accept.restype = c_double

socket_remote_ip = fct.socket_remote_ip
socket_remote_ip.argtypes = [c_double]
socket_remote_ip.restype = c_char_p

socket_send = fct.socket_send
socket_send.argtypes = [c_double]
socket_send.restype = c_double

socket_destroy = fct.socket_destroy
socket_destroy.argtypes = [c_double]
socket_destroy.restype = c_double