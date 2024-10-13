# 10월 26일 목요일 

# 골드4 최단경로
# 클리어

import heapq
from collections import defaultdict 

V, E = map(int, input().split())
K = int(input())

roads = []

for _ in range(E):
  u, v, w = map(int, input().split())
  roads.append([u,v,w])

def shortestPath(roads, start):
  graph = defaultdict(list)
  for road in roads:
    graph[road[0]].append((road[2], road[1]))

  costs = {}
  pq = []

  heapq.heappush(pq,(0,start))

  while pq:
    cur_cost, cur_node = heapq.heappop(pq)
    if cur_node not in costs:
      costs[cur_node] = cur_cost
      for cost, next_node in graph[cur_node]:
        next_cost = cur_cost + cost
        heapq.heappush(pq, (next_cost, next_node))
    
  for i in range(1,V+1): # 기준에서 목적지까지 1부터 모든 최단거리 출력
    if i not in costs.keys(): # 목적지에 도달할 수 없는 경우
      print("INF")
    elif i == start: # 목적지와 출발점이 같은 경우
      print(0)
    else:
      print(costs[i])

shortestPath(roads, K)

