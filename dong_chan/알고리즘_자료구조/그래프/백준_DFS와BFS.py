# 0916 토요일 백준 문제 DFS와 BFS
from collections import deque

N , M , V = map(int,input().split())

# graph = {}

# 간선이 여러개 일 경우 정점이 작은 경우 부터 탐색

# 이건 방향 그래프

# for i in range(M):
#   a, b = input().split()
#   if a not in graph:
#     graph [a] = list(b)
#   else:
#     graph[a].append(b)
#     graph[a] = sorted(graph[a])

graph = [[] for _ in range(N + 1)] # 비어있는 2차원 리스트 선언후

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 값을 대입하는 형식

for i in graph:
  i.sort()


bfs_visited = [False] * (N+1)

def bfs(start_v):
  queue = deque()
  queue.append(start_v)
  bfs_visited[start_v] = True
  print(start_v, end=" ")

  while queue:
    cur_v = queue.popleft()
    for v in graph[cur_v]:
      if not bfs_visited[v]:
        queue.append(v)
        bfs_visited[v] = True
        print(v, end=" ")


dfs_visited = [False] * (N + 1)

def dfs(v):
  dfs_visited[v] = True
  print(v, end=" ")
  for cur_v in graph[v]:
    if not dfs_visited[cur_v]:
      dfs_visited[cur_v] = True 
      dfs(cur_v)

dfs(V)
print()
bfs(V)

# 문제점 1. 낮은 vertex 부터 탐색해야함 sorted 해결
# 문제점 2. 마지막 vertex 탐색 안함
# 2번 문제점 입력받아 만든 딕셔너리가 방향 그래프 이기 때문


# 답안 확인

# 2차원 리스트로 구현
# visited도 2차원 리스트

# 알게된점 : 방향 그래프와 무방향 그래프는 함수코드의 차이가 아닌, 저장 방식의 차이

# 많이 쓰이는 것은 2차원 리스트를 활용하고 visited 는 True로 바꿔주는 형식

# 실력 향상을 위해서는 저장구조, 방문한 리스트를 어떻게 활용할 지 생각하는 것 

# 이번 문제의 출력 값은 중간에 저장할 데이터를 하나 씩 출력하는 형식으로 구현

# 변수명을 일관성 있게 통일하여 코드의 난해함 수정 하기