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
import sys
import heapq


# 다익스트라
def solution(start):
    visited = [1e9 for _ in range(n + 1)] # 최단거리 테이블
    heap = []
    heapq.heappush(heap, [0, start])
    visited[start] = 0
    while heap:
        # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist, num = heapq.heappop(heap) # 거리, 정점 번호

        # 거리가 해당 정점의 저장된 거리보다 크다면 탐색할 필요없음.
        if dist > visited[num]:
            continue

        # 해당 정점과 인접한 정점의 노드를 확인
        for i, j in graph[num]:
            cost = dist + j

            # 인접한 노드를 거쳐서 이동하는 것이 더 빠른 경우
            if cost < visited[i]:
                visited[i] = cost
                heapq.heappush(heap, [cost, i])

    return visited


n, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

# 양방향 그래프 표시
for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
v1, v2 = map(int, sys.stdin.readline().split())

a = solution(1) # 1부터 n까지 다익스트라
b = solution(v1) # v1부터 n까지 다익스트라
c = solution(v2) # v2부터 n까지 다익스트라

# 1-v1-v2-n 경우와 1-v2-v1-n 경우중 최단 거리를 구한다.
answer = min(a[v1] + b[v2] + c[n], a[v2] + c[v1] + b[n])

if answer >= 1e9:
    print(-1)
else:
    print(answer)