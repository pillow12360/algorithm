# 0926 코테 인프런

'''
갈 수 있는 모든 경우의 수 

상단 모서리에서 하단 모서리까지 갈 수 있는 모든 경우의 수를 반환

1. 완전 탐색 풀이

시간 복잡도 상 가능 한지 여부 판단

테스트 케이스의 답이 2 * 10^9 이하

즉 이 말은 최대 값을 주었다는 의미

'''
m =  7
n =  3

grid = [[0]*m for _ in range(n)]

def dfs(r,c):
  uniquePath = 0

  if r == n and c == m:
    return 1

  if r + 1 <= n:
    uniquePath += dfs(r+1,c)
  if c + 1 <= m:
    uniquePath += dfs(r,c+1)

  return uniquePath

