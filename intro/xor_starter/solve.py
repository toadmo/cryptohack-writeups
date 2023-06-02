from pwn import *

one = "label"
two = 13

xored = xor(one, two)
print(xored)
