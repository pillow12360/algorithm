import heapq

# 가중치 그래프 구현
graph = {
  1: [(2,2),(1,4)],
  2: [(1, 3), (9, 5),(6, 6)],
  3: [(4, 6)],
  4: [(3,3), (5, 7)],
  5: [(1, 8)],
  6: [(3, 5)],
  7: [(7, 6), (9,8)],
  8: []
}

# 다익스트라 구현
# 템플릿 처럼 머리에 박을 것
# 문제마다 코드를 수정하며 활용해야 함

def dijkstra(graph, start, final):
  costs = {} # 비용 업데이트
  pq = [] # 우선순위 큐
  heapq.heappush(pq,(0, start)) # 우선순위큐에 시작노드 추가

  while pq:
    cur_cost, cur_v = heapq.heappop(pq)
    if cur_v not in costs: # 방문한적 없다면
      costs[cur_v] = cur_cost # 비용 업데이트
      for cost, next_v in graph[cur_v]: # 연결된 노드 우선순위 큐에 추가
        next_cost = cur_cost + cost
        heapq.heappush(pq, (next_cost, next_v))
        
  return costs[final]

def d