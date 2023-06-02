from pwn import *

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    new_key = ""
    for i in range(len(s)):
        for j in range(len(s[i])):
            new_key = new_key + xor(s[i][j], k[i][j]).decode("ASCII")
    return new_key


print(add_round_key(state, round_key))

