import struct
import uuid
    
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