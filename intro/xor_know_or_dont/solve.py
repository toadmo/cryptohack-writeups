from Crypto.Util.number import *
from pwn import *

enc = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

enc = int(enc, 16)
enc = long_to_bytes(enc)

known = "crypto{"
key = ""

for j in range(len(known)):
    for i in range(256):
        xorBytes = xor(enc, i)
        xorStr = xorBytes.decode()
        if known[j] == xorStr[j]:
            key += chr(i)
            break

print(key)

key = "myXORkey"

decodeBytes = xor(key, enc)

print(decodeBytes.decode())
