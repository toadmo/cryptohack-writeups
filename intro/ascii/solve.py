f = open('input.txt', 'r')

data = f.read().strip().split(', ')

ans = ""

for i in data:
    ans = ans + chr(int(i))

print(ans)
