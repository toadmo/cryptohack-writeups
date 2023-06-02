# p = 29
# ints = [14, 6, 11]

for i in range(29//2):
    if i**2 % 29 == 14:
        print(i, 14)
    if i**2 % 29 == 6:
        print(i, 6)
    if i**2 % 29 == 11:
        print(i, 11)