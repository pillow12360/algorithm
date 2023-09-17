# dfs 방식
# dfs 방식으로 방문 한 다음 방문 하지 못한 방이 있다면 false return


# bfs 방식

# 큐에 방문 순서를 저장할 때 방문 표시를 한다

# DFS
# 시간복잡도 빅오 O(v+e) (vertex, edge) 모든 edge를 방문하면서 if문을 통과하기 때문


# 재귀 이용

# def dfs(graph, cur_v, visited=[]):
#     visited.append(cur_v)
#     for v in graph[cur_v]:
#         if v not in visited:
#             visited = dfs(graph, v, visited)
#     return visited


rooms = [[1, 3], [2,4], [0], [4], [], [3,4]]


def canVisitAllRoomsDFS(rooms):
  # 방문 하면 append
  # visited = set() # 해시 set을 이용해도 시간복잡도가 O(n)
  # visited = {} # 딕셔너리 사용

  # 문제 특성상 인덱스를 사용 
  visited = [False] * len(rooms)

  def dfs(cur_v): # v에 연결되어 있는 모든 vertex에 방문했다고 가정
    visited[cur_v] = True

    for next_v in rooms[cur_v]:
      if visited[next_v] == False: # 개선 사항 있음 리스트 이기 때문에 in 연산자는 시간 복잡도가 크다 O(n)
        dfs(next_v)

  dfs(0)

  if len(visited) == len(rooms):
    return True 
  else:
    return False
  
  # return visited
# print(canVisitAllRooms(rooms))


# 방문한 곳 표시 방법

# 1. 리스트에 저장한 후 if의 in 연산자로 비교 O(n)
# 2. 딕셔너리 자료구조 저장 후 visited[cur_v] = True # (True는 의미없는 값) if 의 in 연산자 사용 O(n)
# 3. 해시 set 을 이용하여  visited = set() 저장 후 if in 연산자 
# 4. 방의 갯 수 만큼 False 리스트를 선언 후 방문 할 때 True로 변경 if문에서 visited[next_v] == False 로 비교
# 1번 방법 이외에 비교할 시 시간 복잡도는 O(1)
from collections import deque

def canVisitAllRoomsBFS(rooms):
  visited = [False] * len(rooms)

  def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
      cur_v = queue.popleft()
      for next_v in rooms[cur_v]:
        if rooms[next_v] == False:
          queue.append(next_v)
          visited[next_v] = True
  
  bfs(0)
  return all(visited) # 파이썬 내장 함수 all 파라미터의 원소들이 모두 참일때 True 아니면 False
print(canVisitAllRoomsBFS(rooms))