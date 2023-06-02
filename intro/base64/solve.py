import base64

f = open('input.txt', 'r')

data = f.read().strip()

byte_string = bytes.fromhex(data)

final = base64.b64encode(byte_string)

print(final)
