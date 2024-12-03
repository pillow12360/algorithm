a = list(map(int, input().split()))

is_answer = True

for i in a:
    if not i % 3 == 0:
        is_answer = False
        break

if is_answer:
    print(1)
else:
    print(0)