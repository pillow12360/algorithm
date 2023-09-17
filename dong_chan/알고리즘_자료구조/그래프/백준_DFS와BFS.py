# 0916 토요일 백준 문제 DFS와 BFS
from collections import deque

N , M , V = map(int,input().split())

graph = []

# 간선이 여러개 일 경우 정점이 작은 경우 부터 탐색


for _ in range(M):
  a = list(map(int,input().split()))
  graph.append(a)

graph = sorted(graph)
print(graph)


for i in range(5):
  if graph[i] == V:
    start_idx = i

bfs_visited = []

def bfs(v):

  queue = deque()
  queue.append(v)
  bfs_visited.append(v)

  while queue:
    cur_v = queue.popleft()
    for v in graph[cur_v]:










