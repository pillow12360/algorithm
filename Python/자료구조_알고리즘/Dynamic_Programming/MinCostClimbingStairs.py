cost = [10,15,20,17,1]

# 완전탐색 재귀 dfs

# O(2^n)
def dfs(n):
  if n == 0 or n == 1:
    return 0

  return min(dfs(n-2)+cost[n-2],dfs(n-1)+cost[n-1])

print(dfs(len(cost)))


# top down dp O(n)

memo = {}

def dp(n):
  if n == 0 or n == 1:
    return 0
  if n not in memo:
    memo[n] = min(dp(n-2)+cost[n-2],dp[n-1]+cost[n-1])
  return memo[n]

# bottom - up 

dp_table = []


