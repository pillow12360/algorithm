# 9월 18일 백준 2번째 문제 바이러스 실버 3

# BFS문제

from collections import deque

computer_count = int(input())

M = int(input())

graph = [[] for _ in range(computer_count+1)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

virus = [False] * (computer_count+1)

def bfs(start_v):
  queue = deque()
  virus[start_v] = True
  queue.append(start_v)
  while queue:
    cur_c = queue.popleft()
    for next_c in graph[cur_c]:
      if not virus[next_c]:
        queue.append(next_c)
        virus[next_c] = True

virus_count = 0

bfs(1)

for i in virus:
  if i == True:
    virus_count += 1

print(virus_count-1)

# DFS 풀이


