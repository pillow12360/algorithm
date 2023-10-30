# 10월 27일 

# 다익스트라 (골드 4) 특정한 최단 경로

'''
입력
첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데, a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000) 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1) 임의의 두 정점 u와 v사이에는 간선이 최대 1개 존재한다.

출력
첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.
'''

# 1번 부터 end 까지
'''
from collections import defaultdict
import heapq

N, E = map(int, input().split())

roads = []

for _ in range(E):
  a, b, c = map(int, input().split())
  roads.append([a,b,c])

must_a, must_b = map(int, input().split())

end = N

def dijkstra(roads,start):
  graph = defaultdict(list)

  for i in roads:
    graph[i[0]].append((i[2],i[1]))

  costs = {}
  pq = []

  heapq.heappush(pq,(0,start))

  while pq:
    cur_cost, cur_node = heapq.heappop(pq)
    if cur_node not in costs:
      costs[cur_node] = cur_cost
      for cost, next_node in graph[cur_node]:
        next_cost = cost + cur_cost
        heapq.heappush(pq,(next_node,next_cost))

  print(f"costs : {costs}")

  return costs[end]

'''

from collections import defaultdict
import heapq

N, E = map(int, input().split())

roads = []

for _ in range(E):
    a, b, c = map(int, input().split())
    roads.append([a, b, c])

must_a, must_b = map(int, input().split())

end = N

def dijkstra(roads, start):
    graph = defaultdict(list)

    for i in roads:
        graph[i[0]].append((i[2], i[1]))

    costs = {}
    pq = []

    heapq.heappush(pq, (0, start))

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if cur_node not in costs:
            costs[cur_node] = cur_cost
            for cost, next_node in graph[cur_node]:
                next_cost = cost + cur_cost
                heapq.heappush(pq, (next_cost, next_node))

    return costs

# 출발지에서 must_a까지의 비용과 must_b까지의 비용 계산
costs_from_start = dijkstra(roads, 1)
cost_to_must_a = costs_from_start[must_a]
cost_to_must_b = costs_from_start[must_b]

# must_a에서 must_b까지의 비용 계산
costs_between_must_a_and_b = dijkstra(roads, must_a)
cost_between_must_a_and_b = costs_between_must_a_and_b[must_b]

# must_b에서 목적지까지의 비용 계산
costs_from_must_b = dijkstra(roads, must_b)
cost_from_must_b_to_end = costs_from_must_b[end]

# 출발지 -> must_a -> must_b -> 목적지 비용과 출발지 -> must_b -> must_a -> 목적지 비용 비교
min_cost = min(cost_to_must_a + cost_between_must_a_and_b + cost_from_must_b_to_end,
               cost_to_must_b + cost_between_must_a_and_b + cost_from_must_b_to_end)

print(min_cost)