from ctypes import *

fct = CDLL("faucet_networking/Faucet Networking.dll")

fct.dllStartup()

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
