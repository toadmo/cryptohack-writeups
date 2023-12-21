from egcd import egcd
from Crypto.Util.number import *
from functools import reduce
from gmpy2 import iroot
from itertools import combinations

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

f = open('inp.txt', 'r')

n_list = []
ct_list = []

for line in f.readlines():
    if line[0] == "n":
        n_list.append(int(line.split(' = ')[1]))
    if line[0] == "c":
        ct_list.append(int(line.split(' = ')[1]))

for i, j, k in combinations(range(7), 3):
    ns = [n_list[i], n_list[j], n_list[k]]
    cs = [ct_list[i], ct_list[j], ct_list[k]]
    m_cubed = chinese_remainder(ns, cs)
    m = iroot(m_cubed, 3)
    if m[1] == True:
        print(long_to_bytes(m[0]))
        break
