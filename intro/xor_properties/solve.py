from pwn import *
from Crypto.Util.number import *

k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
k2k1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
k2k3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flagk13k2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

k1 = int(k1, 16)
k2k1 = int(k2k1, 16)
k2k3 = int(k2k3, 16)
flagk13k2 = int(flagk13k2, 16)

k1 = long_to_bytes(k1)
k2k1 = long_to_bytes(k2k1)
k2k3 = long_to_bytes(k2k3)
flagk13k2 = long_to_bytes(flagk13k2)

flag = xor(xor(flagk13k2, k2k3), k1)
print(flag)
