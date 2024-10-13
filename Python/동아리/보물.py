N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

# 1 <= N <= 50
# 0<= A <= 100

# 가장 작게 되려면
# 가장 큰 수와 가장 작은 수 의 곱의 합

# 0 x 가장 큰 수

A.sort()
B.sort(reverse=True)

S = 0

for i in range(N):
  S += A[i] * B[i]

print(S)
