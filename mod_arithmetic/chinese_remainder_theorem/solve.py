# x ≡ 2 mod 5
# x ≡ 3 mod 11
# x ≡ 5 mod 17

from sympy.ntheory.modular import crt

print(crt([5, 11, 17], [2, 3, 5]))