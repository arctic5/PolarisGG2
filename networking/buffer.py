import struct
import uuid
import sys
sys.path.append("../")
import constants

class Buffer:
    def __init__(self):
        self.pos = 0
        self.endianness = constants.ENDIAN_LITTLE
        self.bufferString = ""
    def write(self, type, data):
        self.bufferString += str(struct.pack(self.endianness + type, data))
        return 0
    def read(self, type):
        if (self.pos >= len(self.bufferString)):
            return None
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
def write_directly_to_buffer(buf, data):
    buf.bufferString += data
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
    format += str(len(string)) + 's'
    write_directly_to_buffer(buf, str(struct.pack(buf.endianness + format, string)))
    return 0
def read_string(buf, size):
    format = ''
    while (len(format) < size):
        format += 's'
    str = struct.unpack_from(buf.endianness + format, buf.bufferString, buf.pos)
    buf.pos += struct.calcsize(buf.endianness + format)
    return ''.join(str)
def buffer_clear(buf):
    buf.bufferString = ''
    
#that other crap gg2 uses
def writeKeyValue(handle, key, value):
    if(len(key) > 255):
        print "ERROR: KEY TOO LONG"
    if(len(value) > 65535):
        value = value[:65535]
    write_ubyte(handle, len(key))
    write_string(handle, key)
    write_ushort(handle, len(value))
    write_string(handle, value)
    return 0
    
def parseUuid(uuidString, buf):
    ID = uuid.UUID(uuidString)
    write_directly_to_buffer(buf, ID.get_bytes())
    return 0
def buffer_destroy(buf):
    buf = None
    del buf
    return 0