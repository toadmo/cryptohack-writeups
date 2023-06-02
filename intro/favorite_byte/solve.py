from Crypto.Util.number import *
from pwn import *

inp = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

inp = int(inp, 16)
inp = long_to_bytes(inp)

for i in range(256):
    byteStr = xor(i, inp)
    try:
        print(byteStr.decode())
    except:
        print("bad string")
