# 8월10일 회의실 배정

N = int(input())

list = []

while N > 0:
    A, B = map(int, input().split())
    list.append(B - A)
    N -= 1

print(list)
