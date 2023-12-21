from factordb.factordb import FactorDB

n = 510143758735509025530880200653196460532653147

f = FactorDB(n)

f.connect()

factors = f.get_factor_list()

print(min(factors))