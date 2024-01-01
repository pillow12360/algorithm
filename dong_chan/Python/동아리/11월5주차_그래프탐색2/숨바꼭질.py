from collections import deque

n , k = map(int, input().split())

MAX = 10 ** 5

dist = [0] * (MAX + 1)

def bfs():
  q = deque()
  q.append(n)
  while q:
    x = q.popleft()
    if x == k:
      print(dist[x])
      break
    for next_x in (x-1, x+1 , x* 2):
      if 0 <= next_x <= MAX and not dist[next_x]:
        dist[next_x] = dist[x] + 1
        q.append(next_x)

bfs()
