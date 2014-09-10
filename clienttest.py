#from networking from buffer import *
import socket
global tcpListener

hostingPort = 8190
attemptPortForward = 1

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print "error"

class ClientTest:
    def __init__(self):
        sock.connect(("127.0.0.1", hostingPort))
        sock.sendall("HIIIIIIII")
        data = sock.recv(1024)
        sock.close()
        print 'Received', repr(data)
if __name__ == '__main__':
    server = ClientTest()