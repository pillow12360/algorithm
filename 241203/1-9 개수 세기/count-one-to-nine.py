n = int(input())

a = list(map(int,input().split()))

answer = [0] * 9

for i in a:
    answer[i-1] += 1



print("\n".join(map(str,answer)))