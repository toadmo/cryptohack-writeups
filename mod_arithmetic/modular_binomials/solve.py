from factordb.factordb import FactorDB

f = open("data_04a0fe134cf31a6c941377aad75db81c.txt", "r")

data = f.read().strip()

exec(data)

f = FactorDB(N)

f.connect()
print(f.get_factor_from_api())

