import socket
import buffer as b

def send(sock, buffer):
    sock.send(buffer.bufferString)
    
# container thing for socket stuff
class Socket:
    def __init__(self, ip, socket_id):
        self.ip = -1
        self.socket_id = -1
        self.buffer = b.buffer_create()