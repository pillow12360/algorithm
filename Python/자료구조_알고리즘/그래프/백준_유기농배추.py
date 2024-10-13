# 10월 6일 유기농 배추 (그래프) 실버2

# bfs 풀이
'''
from collections import deque

t = int(input())

# 가로 m (c)
# 세로 n (r)

while t > 0:

  m, n, k = map(int,input().split())

  ground = [[0] * (m) for _ in range(n)]
  visited = [[False] * (m) for _ in range(n)]

  for i in range(k):
    c, r = map(int, input().split())
    ground[r][c] = 1

  bug = 0

  def bfs(r, c):

    visited[r][c] = True

    queue = deque()
    queue.append((r,c))

    dy = [1,-1,0,0]
    dx = [0,0,-1,1]

    while queue:
      cur_r , cur_c = queue.popleft()
      for i in range(4):
        next_r = cur_r + dy[i]
        next_c = cur_c + dx[i]
        if next_r >= 0 and next_r < n and next_c >= 0 and next_c < m:
          if visited[next_r][next_c] != True and ground[next_r][next_c] == 1:
            visited[next_r][next_c] = True
            queue.append((next_r,next_c))

  for r in range(n):
    for c in range(m):
      if ground[r][c] == 1 and not visited[r][c]:
        bfs(r,c)
        bug += 1

  print(bug)

  t -= 1
'''

# dfs 풀이

import sys
sys.setrecursionlimit(10**6)

t = int(input())

while t > 0:

  m, n, k = map(int,input().split())

  ground = [[0] * (m) for _ in range(n)]
  visited = [[False] * (m) for _ in range(n)]

  for i in range(k):
    c, r = map(int, input().split())
    ground[r][c] = 1

  bug = 0

  def dfs(r, c):
    visited[r][c] = True
    
    delta = [(1,0),(0,1),(-1,0),(0,-1)]

    for dy , dx in delta:
      nr, nc = r + dy, c + dx
      if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and ground[nr][nc] == 1:
        dfs(nr, nc)

  for r in range(n):
    for c in range(m):
      if ground[r][c] == 1 and not visited[r][c]:
        dfs(r,c)
        bug += 1

  print(bug)

  t -= 1
