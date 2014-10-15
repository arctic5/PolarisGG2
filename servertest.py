from buffer import *
import socket
hostingPort = 8190

class ServerTest:
    def __init__(self):
        try:
            self.tcpListener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as msg:
            print "error"
        self.tcpListener.bind(("127.0.0.1", hostingPort))
        self.tcpListener.listen(1)
        self.tcpListener.setblocking(0)
        print "serving on port:",hostingPort
        a = buffer_create()
    def step(self):
        try:
            self.joiningSocket, self.joiningIP = self.tcpListener.accept()
            print "GOT A CONNECTION"
            print "IP:", joiningIP
            try:
                write_ubyte(a, 7)
            except:
                raise
            try:
                self.data = self.joiningSocket.recv(1024)
                self.joiningSocket.sendall(data)
                self.joiningSocket.close()
            except:
                pass
        except:
            pass
        
if __name__ == '__main__':
    server = ServerTest()
    while True:
        server.step()