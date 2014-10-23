import socket

def send(sock, buffer):
    sock.send(buffer.bufferString)