from collections import deque
import struct

# create a dict to store buffers
global __buffers = {}

def buffer_create():
    bufId = len(__buffers) + 1
    __buffers[bufId] = ""
    return bufId
def write_ubyte(buffer, data, bigEndian=False):
    if (bigEndian == False):
        __buffers[buffer] += str(struct.pack("<B", data))
    else:
        __buffers[buffer] += str(struct.pack(">B", data))
    return 0
def write_byte(buffer, data, bigEndian=False):
    if (bigEndian == False):
        __buffers[buffer] += str(struct.pack("<b", data))
    else:
        __buffers[buffer] += str(struct.pack(">b", data))
    return 0
def write_ushort(buffer, data, bigEndian=False):
    if (bigEndian == False):
        __buffers[buffer] += str(struct.pack("<H", data))
    else:
        __buffers[buffer] += str(struct.pack(">H", data))
    return 0
def write_short(buffer, data, bigEndian=False):
    if (bigEndian == False):
        __buffers[buffer] += str(struct.pack("<h", data))
    else:
        __buffers[buffer] += str(struct.pack(">h", data))
    return 0
def write_uint(buffer, data, bigEndian=False):
    if (bigEndian == False):
        __buffers[buffer] += str(struct.pack("<I", data))
    else:
        __buffers[buffer] += str(struct.pack(">I", data))
    return 0
def write_int(buffer, data, bigEndian=False):
    if (bigEndian == False):
        __buffers[buffer] += str(struct.pack("<i", data))
    else:
        __buffers[buffer] += str(struct.pack(">i", data))
    return 0
def write_float(buffer, data, bigEndian=False):
    if (bigEndian == False):
        __buffers[buffer] += str(struct.pack("<f", data))
    else:
        __buffers[buffer] += str(struct.pack(">f", data))
    return 0
def write_double(buffer, data, bigEndian=False):
    if (bigEndian == False):
        __buffers[buffer] += str(struct.pack("<d", data))
    else:
        __buffers[buffer] += str(struct.pack(">d", data))
    return 0
def read_ubyte(buffer, bigEndian=False):
    if (bigEndian == False):
        return struct.unpack("<B", __buffers[buffer])
    else:
        return struct.unpack(">B", __buffers[buffer])
def read_byte(buffer, bigEndian=False):
    if (bigEndian == False):
        return struct.unpack("<b", __buffers[buffer])
    else:
        return struct.unpack(">b", __buffers[buffer])
def read_ushort(buffer, bigEndian=False):
    if (bigEndian == False):
        return struct.unpack("<H", __buffers[buffer])
    else:
        return struct.unpack(">H", __buffers[buffer])
def read_short(buffer, bigEndian=False):
    if (bigEndian == False):
        return struct.unpack("<h", __buffers[buffer])
    else:
        return struct.unpack(">h", __buffers[buffer])
def read_uint(buffer, bigEndian=False):
    if (bigEndian == False):
        return struct.unpack("<I", __buffers[buffer])
    else:
        return struct.unpack(">I", __buffers[buffer])
def read_int(buffer, bigEndian=False):
    if (bigEndian == False):
        return struct.unpack("<i", __buffers[buffer])
    else:
        return struct.unpack(">i", __buffers[buffer])
def read_float(buffer, bigEndian=False):
    if (bigEndian == False):
        return struct.unpack("<f", __buffers[buffer])
    else:
        return struct.unpack(">f", __buffers[buffer])
def read_double(buffer, bigEndian=False):
    if (bigEndian == False):
        return struct.unpack("<d", __buffers[buffer])
    else:
        return struct.unpack(">d", __buffers[buffer])

    