# 9월 18일 dfs , bfs 단지번호 붙이기 실버1

from collections import deque

M = int(input())

house = []

visited = [[False] * M for _ in range(M)]

size_list = []

for _ in range(M):
  a = list(input())
  house.append(a)

house_len = M

delta = [(1,0),(-1,0),(0,-1),(0,1)] # 상하좌우

def bfs(start_h,size_list):
  r , c = start_h
  queue = deque()
  size = 1
  queue.append((r,c))
  visited[r][c] = True

  while queue:
    cur_r , cur_c = queue.popleft()

    for dr , dc in delta:
      next_r = cur_r + dr
      next_c = cur_c + dc
      if next_r >= 0 and next_r < M and next_c >= 0 and next_c < M:
        if house[next_r][next_c] == '1' and not visited[next_r][next_c]:
          queue.append((next_r, next_c))
          visited[next_r][next_c] = True
          size += 1

  size_list.append(size)

house_count = 0

for r in range(M):
  for c in range(M):
    if house[r][c] == '1' and not visited[r][c]:
      bfs((r,c),size_list)
      house_count += 1

print(house_count)

size_list.sort()

for i in size_list:
  print(i)