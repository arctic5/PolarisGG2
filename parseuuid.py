from faucet_networking import buffer
import uuid
import struct
def parseUuid(string, buffer):
    b = buffer.buffer_create()
    bytes = struct.unpack(uuid.UUID(string).bytes)
    for (i in bytes):
        buffer.write_ubyte(i)