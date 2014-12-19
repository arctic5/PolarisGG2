from faucet_networking.buffer import *

a = buffer_create()
b = buffer_create()

print a
print b

print write_ubyte(a, 1)
print write_ubyte(b, 2)
