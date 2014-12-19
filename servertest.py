from faucet_networking.buffer import *
from faucet_networking.socket import *
import constants
hostingPort = 8190

class ServerTest:
    def __init__(self):
        self.tcpListener = tcp_listen(8190)
        if (socket_has_error(self.tcpListener)):
            print "error"
        print "serving on port:",hostingPort
        a = buffer_create()
    def step(self):
        self.joiningSocket = socket_accept(self.tcpListener)
        if (self.joiningSocket >= 0):
            self.ip = socket_remote_ip(self.joiningSocket)
            print ip
            write_ubyte(self.joiningSocket, constants.KICK)
            write_ubyte(self.joiningSocket, constants.KICK_MULTI_CLIENT)
            socket_send(self.joiningSocket)
            socket_destroy(self.joiningSocket)
if __name__ == '__main__':
    server = ServerTest()
    while True:
        server.step()

