import struct
class Buffer:
    def __init__(self):
        self.pos = 0
        # < small
        # > big
        self.endianness = "<"
        self.bufferString = ""
    def write(self, type, data):
        self.bufferString += str(struct.pack(self.endianness + type, data))
        return 0
    def read(self, type):
        if (self.pos >= len(self.bufferString)):
            return -1
        else:
            r = struct.unpack_from(self.endianness + type, self.bufferString, self.pos)
            self.pos += struct.calcsize(self.endianness + type)
            return r
    def get_buf_string(self):
        return self.bufferString
def buffer_create():
    return Buffer()
def write_ubyte(buf, data):
    return buf.write("B", data)
def write_byte(buf, data):
    return buf.write("b", data)
def write_ushort(buf, data):
    return buf.write("H", data)
def write_short(buf, data):
    return buf.write("h", data)
def write_uint(buf, data):
    return buf.write("I", data)
def write_int(buf, data):
    return buf.write("i", data)
def write_float(buf, data):
    return buf.write("f", data)
def write_double(buf, data):
    return buf.write("d", data)
def read_ubyte(buf):
    return buf.read("B")[0]
def read_byte(buf):
    return buf.read("b")[0]
def read_ushort(buf):
    return buf.read("H")[0]
def read_short(buf):
    return buf.read("h")[0]
def read_uint(buf):
    return buf.read("I")[0]
def read_int(buf):
    return buf.read("i")[0]
def read_float(buf):
    return buf.read("f")[0]
def read_double(buf):
    return buf.read("d")[0]