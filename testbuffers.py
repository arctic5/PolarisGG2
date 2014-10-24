from ctypes import *

fct = CDLL("Faucet Networking.dll")

fct.dllStartup()

buffer_create = fct.buffer_create
buffer_create.restype = c_double

write_ubyte = fct.write_ubyte
write_ubyte.argtypes = [c_double, c_double]
write_ubyte.restype = c_double

a = buffer_create()
b = buffer_create()

print a
print b

print write_ubyte(a, 1)
print write_ubyte(b, 2)