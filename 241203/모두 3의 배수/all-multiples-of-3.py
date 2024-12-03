
n = 5

answer = True

for _ in range(n):
    a = int(input())

    if a % 3 != 0:
        answer = False
        break

if answer:
    print(1)
else:
    print(0)