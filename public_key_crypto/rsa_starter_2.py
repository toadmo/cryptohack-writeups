# "Encrypt" the number 12 using the exponent e = 65537 and the primes p = 17 and q = 23. What number do you get as the ciphertext?

p = 17
q = 23
n = p*q
e = 65537
pt = 12

ct = pow(pt, e, n)

print(ct)