f = open('input.txt', 'r')

data = f.read().strip()

bytes_object = bytes.fromhex(data)

text_string = bytes_object.decode("ASCII")

print(text_string)
