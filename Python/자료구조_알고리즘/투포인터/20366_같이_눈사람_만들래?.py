n = int(input())

m = list(map(int, input().split()))

m = sorted(m)

l = len(m) - 1

for i in range(l, -1, -1):
  
  for j in range(i, -1, -1):
    print(i)
