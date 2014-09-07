import socket

def tcp_listen(port):
    try:
        asdf = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        asdf.bind((127.0.0.1, port))
        asdf.listen(1)
        asdf.setblocking(0)
        return asdf
    except:
        return -1
def tcp_connect(ip, port):
    try:
        asdf = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        try:
            asdf = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        except:
            return -1
    try:
        asdf.connect((ip, port))
        asdf.setblocking(0)
        return asdf
    except:
        return -1
# lol
def socket_accecpt(handle):
    socket, ip = handle.accecpt 
    return socket, ip
def socket_send(handle, buffer):
    pass