'''
주어진 네트워크에는 n개의 노드가 있으며, 이는 1부터 n까지 레이블이 붙어 있습니다. 또한 times[i] = (ui, Vi, Wi)
리스트가 주어집니다. 이 때, ui 노드에서 신호를 보내 vi 노드에 도달하는데 걸리는 시간을 wi 라고 합니다.

k노드에서 신호를 보낼 때, 모든 노드에 신호가 도달하기 위한 최소 비용을 반환하시오. 하나의 노드라도 도달하지 못한다면, -1을 반한하시오 (한 노드에서 연결된 여러개의 edge에 신호를 동시에 전달할 수 있습니다.)
'''
import heapq
from collections import defaultdict
times = [
  [2,1,2],
  [2,3,5],
  [2,4,1],
  [4,3,3]
]
n = 4
k = 2


# 그래프 구현
def networkDelayTime(times, n, k):
  graph = defaultdict(list) # 딕셔너리 선언
  
  for time in times:
    graph[time[0]].append((time[2], time[1]))

  costs = {}
  pq = []
  heapq.heappush(pq,(0,k))

  while pq:
    cur_cost, cur_node = heapq.heappop(pq)
    if cur_node not in costs:
      costs[cur_node] = cur_cost
      for cost, next_node in graph[cur_node]:
        next_cost = cur_cost + cost
        heapq.heappush(pq, (next_cost, next_node))

  for node in range(1, n+1):
    if node not in costs:
      return -1
  return max(costs.values())

print(networkDelayTime(times,n,k))
