# 주사위는 1~6

answer = [0] * 6

a = list(map(int,input().split()))

for i in a:
    answer[i-1] += 1

for i,j in enumerate(answer):
    print(f'{i+1} - {j}')