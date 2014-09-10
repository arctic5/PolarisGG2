from networking import buffer 
import socket
hostingPort = 8190
try:
    tcpListener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print "error"
class ServerTest:
    def __init__(self):
        serverSocket = -1
        tcpListener.bind(("127.0.0.1", hostingPort))
        tcpListener.listen(1)
        #tcpListener.setblocking(0)
        print "serving on port:",hostingPort
        
        joiningSocket, joiningIP = tcpListener.accept()
        print "GOT A CONNECTION"
        print "IP:", joiningIP
        
        while True:
            data = joiningSocket.recv(1024)
            if (not data):
                break
            joiningSocket.sendall(data)
        joiningSocket.close()
if __name__ == '__main__':
    server = ServerTest()