import math

N = int(input())

A = list(map(int, input().split()))

C, B = map(int, input().split())

# print(N,A)

answer = 0

for i in range(len(A)):
  if A[i] >= C:
    answer += 1
    A[i] = A[i] - C

for i in range(len(A)):
  if A[i] >= 0:
    answer += math.ceil(A[i] / B)

print(answer)


list.sort(key=lambda x : x[1])