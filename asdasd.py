from faucetnet import *
from ctypes import *

global protocolUuid
global gg2lobbyId

dllStartup()

protocolUuid = c_double(faucetnet.buffer_create()).value

print protocolUuid

gg2lobbyId = c_double(faucetnet.buffer_create()).value

print gg2lobbyId
hostingPort = 0
print hostingPort
tcpListener = tcp_listen(hostingPort)
print tcpListener
# print buffer_destroy(1.0)

class GameServer:
    def __init__(self):
        ttcpListener = c_double(1)
        print ttcpListener
if __name__ == '__main__':
    server = GameServer()