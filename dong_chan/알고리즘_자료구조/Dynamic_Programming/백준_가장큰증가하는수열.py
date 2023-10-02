N = int(input())
A = list(map(int,input().split()))

def dfs(n):
  length = 1

  if n == len(A)-1:
    return length
  
  a = n
  number = A[a]

  while a < len(A)-1:
    a += 1
    next_number = A[a]
    if number < next_number:
      number = A[a]
      length += 1
    
  if n < len(A)-1:
    length = max(dfs(n+1), length)
  
  return length

print(dfs(0))

# bottom - up 방식

N = int(input())

A = list(map(int, input().split()))

dp_table = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp_table[i] = max(dp_table[i], dp_table[j]+1)

print(max(dp_table))