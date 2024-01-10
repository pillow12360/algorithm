# 1월 4일 DP 다리 놓기

# 실버5

# dp table bottom up 방식

T = int(input())

while T > 0:
  N, M = map(int,input().split())
  
  T -= 1

  dp= [[0]*M for _ in range(N)]

  for i in range(M):
    dp[0][i] = i+1

  for i in range(1,N):
    for j in range(1,M):
      if i == j:
        dp[i][j] = 1
      elif i > j:
        dp[i][j] = 0
      elif i < j:
        dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

  print(dp[-1][-1])