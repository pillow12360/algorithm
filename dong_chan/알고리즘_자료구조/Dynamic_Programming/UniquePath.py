# 0926 코테 인프런

'''
갈 수 있는 모든 경우의 수 

상단 모서리에서 하단 모서리까지 갈 수 있는 모든 경우의 수를 반환

1. 완전 탐색 풀이

시간 복잡도 상 가능 한지 여부 판단

테스트 케이스의 답이 2 * 10^9 이하

즉 이 말은 최대 값을 주었다는 의미

'''

m = 3
n = 7

def dfs(r, c):
  if r == 2 and c == 6: # base 케이스, 끝 부분에 도달 하였을 때
    return 1

  unique_paths = 0

  if r + 1 < 3: # grid의 값이 넘어가지 않도록
    unique_paths += dfs(r+1,c)
  if c + 1 < 7:
    unique_paths += dfs(r,c+1)

  return unique_paths

# 위 코드는 0,0 기준으로 짠 코드이다.

# 도착점을 기준으로 짠 dfs

memo = {}

def dfs(r,c):

  if r == 0 and c == 0:
    memo[(r,c)] = 1
    return memo[(r,c)]
  unique_paths = 0
  if (r, c) not in memo:
    if r - 1 >= 0:
      unique_paths += dfs(r-1, c)
    if c - 1 >= 0:
      unique_paths += dfs(r, c-1)
    memo[(r,c)] = unique_paths
  return memo[(r,c)]

# 현재 코드는 중복되는 계산값이 존재하는지 확인해 보자


# 2중리스트를 활용한 memo

def uniquePaths(m,n):
  memo = [[-1]* n for _ in range(m)]
  def dfs(r,c):
    if r == 0 and c == 0:
      memo[r][c] = 1
      return memo[r][c]

    unique_paths = 0

    if memo[r][c] == -1:
      if r - 1 >= 0:
        unique_paths += dfs(r-1, c)
      if c - 1 >= 0:
        unique_paths += dfs(r, c-1)
      memo[r][c] = unique_paths
    return memo[r][c]

  return dfs(m-1,n-1)


# bottom - up 방식으로 구현

def uniquePaths(m, n):
  memo = [[-1] * n for _ in range(m)]

  for r in range(m): # 왼쪽 위 가장자리 1로 초기화
    memo[r][0] = 1
  for c in range(n):
    memo[0][c] = 1

  for r in range(m): # 점화식으로 dp table 채우기
    for c in range(n):
      memo[r][c] = memo[r-1][c] + memo[r][c-1]

  return memo[m-1][n-1]