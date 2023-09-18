# 출발점 (0,0) 도착점 (N-1, M-1)

# 그래프

from collections import deque

N = 5
M = 6

graph = [[0]*N for _ in range(M)]
# person = [[False]*N for _ in range(M)]

x = [(2,1),(3,3)]

for y,x in x:
  graph[y][x] = 'x'

# 줄을 붙어서 설 수 없는 경우를 고려해야함
# 한개로 이어지는 것이 아닌 두개로 이어 지면 안됨

def bfs(graph):
  length_list = []

  queue = deque()
  queue.append((0,0,1))
  graph[0][0] = 1
  
  delta = [(1,0),(-1,0),(0,-1),(0,1)]

  while queue:
    cur_y , cur_x, length = queue.popleft()

    if cur_y == M-1 and cur_x == N-1:
      length_list.append(length) 

    for dy, dx in delta:
      next_y = cur_y + dy
      next_x = cur_x + dx

      if next_y >= 0 and next_y < M and next_x >= 0 and next_x < N:
        if graph[next_y][next_x] == 0 and graph[next_y][next_x] != 'x':
          queue.append((next_y,next_x, length+1))
          graph[next_y][next_x] = 1

  return length_list

# print(bfs(graph))
# print(graph)

# 최단거리를 구하는 것 이 아닌 최장 거리를 구해야 함

