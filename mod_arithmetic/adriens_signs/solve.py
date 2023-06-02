# If bit is 1, then the number is a quadratic residue
# Check with the Legendre symbol

a = 288260533169915
p = 1007621497415251

f = open("output_80fc6398d2fd9f272186d0af510323f9.txt", "r")

data = f.read().strip()

ct = eval(data)

def decrypt_flag(ciphertext):
    binpt = ""
    pt = ""
    for bit in ciphertext:
        if pow(bit,(p-1)//2,p) == 1:
            binpt = binpt + "1"
        else:
            binpt = binpt + "0"

    for i in range(0, len(binpt), 8):
        pt = pt + chr(int(binpt[i:i+8], 2))
    
    print(pt)

decrypt_flag(ct)