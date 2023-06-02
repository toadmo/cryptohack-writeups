f = open("output_479698cde19aaa05d9e9dfca460f5443.txt", "r")

data = f.read()

p, ints  = data.split("\n\n")

exec(p)
exec(ints)

for int in ints:
    legendre = pow(int,(p-1)//2,p)
    if legendre == 1:
        # fermats little theorem
        print(pow(int, (p+1)//4, p))