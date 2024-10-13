# 0916 그래프 bfs 최단거리를 활용한 문제

from collections import deque

N , M = map(int,input().split())

grid = []

for i in range(N):
  a = input()
  grid.append(list(a))


def shortest_path_miro(grid):
  shortest_path = 1

  row = len(grid)
  col = len(grid[0])

  queue = deque()
  queue.append((0,0,1))

  visited = [[False]*col for _ in range(row)]

  visited[0][0] = True

  delta = [(1,0),(-1,0),(0,1),(0,-1)]

  while queue:
    cur_r , cur_c , cur_len = queue.popleft()

    if cur_r == row-1 and cur_c == col - 1:
      shortest_path = cur_len

    for dr,dc in delta:
      next_r = cur_r + dr
      next_c = cur_c + dc

      if next_r >= 0 and next_r < row and next_c >= 0 and next_c < col:
        if grid[next_r][next_c] == "1" and not visited[next_r][next_c]:
          queue.append((next_r,next_c,cur_len+1))
          visited[next_r][next_c] = True

  return shortest_path

print(shortest_path_miro(grid))