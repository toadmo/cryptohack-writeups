from factordb.factordb import FactorDB
from egcd import egcd
from Crypto.Util.number import long_to_bytes

n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373


f = FactorDB(n)

f.connect()

[p,q] = f.get_factor_list()

tot = (p-1)*(q-1)

d = egcd(e, tot)[1]

pt_long = pow(ct, d, n)

pt = long_to_bytes(pt_long)

print(pt)