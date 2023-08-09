# 8월 9일 2번째 문제 11시 51분

N , K = map(int,input().split())

A = []

dap = 0

while N > 0:
    a = int(input())
    A.append(a)
    N -= 1

A.sort(reverse=True)

for i in range(len(A)):
      if K-A[i] >= 0:
          while K >= A[i]:
            K -= A[i]
            dap += 1
      elif K < 0:
          break

print(dap)