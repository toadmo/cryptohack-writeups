from Crypto.Util.number import *

f = open('input.txt', 'r')

num = f.read().strip()

b10 = int(num)

byteNum = long_to_bytes(b10)

print(byteNum)
