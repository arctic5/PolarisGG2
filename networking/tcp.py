import socket

def socket_send(sock, buffer):
    sock.send(buffer.bufferString)