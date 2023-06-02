a = 66528
b = 52920

def gcd(a, b):
    big = max([a,b])
    small = min([a,b])
    if big % small == 0:
        return max([big/small, small])
    else:
        return gcd(small, big % small)

print(gcd(a, b))