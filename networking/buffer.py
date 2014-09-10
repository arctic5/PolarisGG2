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
            return r[0]
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
    return buf.read("B")
def read_byte(buf):
    return buf.read("b")
def read_ushort(buf):
    return buf.read("H")
def read_short(buf):
    return buf.read("h")
def read_uint(buf):
    return buf.read("I")
def read_int(buf):
    return buf.read("i")
def read_float(buf):
    return buf.read("f")
def read_double(buf):
    return buf.read("d")
#slightly more complicated thing for string
#maybe even overcomplicated but whatever
def write_string(buf, string):
    format = ''
    size = len(str(string))
    while (size > 0):
        format += 'c'
        size -= 1
    data = list(string)
    buf.bufferString += str(struct.pack(buf.endianness + format, *data))
    return buf.bufferString
def read_string(buf, size):
    sizeBkp = size
    format = ''
    while (size > 0):
        format += 'c'
        size -= 1
    str = struct.unpack_from(buf.endianness + format, buf.bufferString, buf.pos)
    buf.pos += struct.calcsize(buf.endianness + format)
    return ''.join(str)