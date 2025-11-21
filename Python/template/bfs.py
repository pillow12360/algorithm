from collections import deque

answer = []

dr = [1,-1,0,0]
dc = [0,0,-1,1]

grid = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
# 상하좌우

# 인덱스 범위 판별
def is_range(r,c):
  return 0<= r < n and 0<= c < m


def bfs(r,c):
  q = deque((r,c))
  visited[r][c] = True

  while q:
    cr, cc = q.popleft()

    for i in range(4):
      nr = dy[i] + cr
      nc = dc[i] + cc

      if is_rage(nr,nc):
        if not visited[nr][nc] and grid[nr][nc] == 1:
          q.append([nr,nc])
          visitied[nr][nc] = False
          answer.append([nr,nc])


print(answer)