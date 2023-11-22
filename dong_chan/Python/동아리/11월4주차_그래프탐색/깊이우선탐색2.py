'''
오늘도 서준이는 깊이 우선 탐색(DFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다. 정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

깊이 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 내림차순으로 방문한다.
'''

'''



def dfs(cur_v):  # dfs 구현
    visited.append(cur_v)
    dap.append(cur_v)
    for next_v in graph[cur_v]:
        if next_v not in visited:
            dfs(next_v)


N, M, R = map(int, input().split())  # N : 노드 개수 , M : 간선 개수 , R 시작 노드

visited = []

graph = {}  # 인접리스트

for i in range(M):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)

    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)

for i in graph:
    graph[i].sort(reverse=True)

dap = []

# print(graph)  # 그래프 확인
dfs(R)
# print(visited)

if (N-len(dap) > 0):
    for i in range(N-len(dap)):
        dap.append(0)

for i in dap:
    print(i)
'''

'''
N, M, R = map(int, input().split())

graph = {}

for i in range(M):
    a, b = map(int, input().split())
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)

for neighbors in graph.values():
    neighbors.sort(reverse=True)

visited = set()
result = []


def dfs(cur_v):
    visited.add(cur_v)
    result.append(cur_v)
    for next_v in graph[cur_v]:
        if next_v not in visited:
            dfs(next_v)


dfs(R)

result += [0] * (N - len(result))

for i in result:
    print(i)
'''


N, M, R = map(int, input().split())

graph = [[] * (N + 1) for _ in range(N+1)]  # 0번재 인덱스는 사용 x
# 2중 리스트 초기화

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 양방향 그래프

for i in range(1, N+1):
    graph[i].sort(reverse=True)  # 내림차순으로 탐색 구현

# print(graph)

visited = [0] * (N + 1)


def dfs(x):
    global cnt
    cnt += 1
    visited[x] = 1
    node_cnt[x] = cnt
    for i in graph[x]:
        if not visited[i]:
            dfs(i)


node_cnt = [0] * (N + 1)  # 0 부터 시작함으로 +1
cnt = 0
# 방문한 순서로 저장하기 위한 cnt

dfs(R)

for i in node_cnt[1:]:
    print(i)
