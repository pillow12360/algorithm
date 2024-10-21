num = list(map(int, input().split()))

a = num[0]
b = num[1]
c = num[2]
d = num[3]
e = num[4]
f = num[5]

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            break
    else:
        continue
    break
