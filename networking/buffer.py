import struct
class Buffer:
    def __init__(self):
        self.pos = 0
        self.bigEndian = False
        self.bufferString = ""
        return self.id()
    def write(self, type, data):
        if (self.bigEndian == False):
            self.bufferString += str(struct.pack("<" + type, data)
        else:
            self.bufferString += str(struct.pack(">" + type, data)
        return 0
    def read(self, type):
        if (self.bigEndian == False):
            if (self.pos >= len(self.bufferString)):
                return -1   
            else:
                r = struct.unpack_from("<" + type, self.bufferString, self.pos)
                self.pos += 1
                return r
    def get_buf_string(self):
        return self.bufferString
def buffer_create():
    return Buffer()
def write_ubyte(buffer, data):
    return buffer.write("B", data)
def write_byte(buffer, data):
    return buffer.write("b", data)
def write_ushort(buffer, data):
    return buffer.write("H", data)
def write_short(buffer, data):
    return buffer.write("h", data)
def write_uint(buffer, data):
    return buffer.write("I", data)
def write_int(buffer, data):
    return buffer.write("i", data)
def write_float(buffer, data):
    return buffer.write("f", data)
def write_double(buffer, data):
    return buffer.write("d", data)
def read_ubyte(buffer):
    return buffer.read("B")
def read_byte(buffer):
    return buffer.read("b")
def read_ushort(buffer):
    return buffer.read("H")
def read_short(buffer):
    return buffer.read("h")
def read_uint(buffer):
    return buffer.read("I")
def read_int(buffer):
    return buffer.read("i")
def read_float(buffer):
    return buffer.read("f")
def read_double(buffer):
    return buffer.read("d")

    