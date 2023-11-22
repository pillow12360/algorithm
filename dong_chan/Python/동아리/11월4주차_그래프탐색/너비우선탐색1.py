from collections import deque

N, M, R = map(int, input().split())

graph = [[]*(N+1) for _ in range(N+1)]  # 양방향 그래프 구현

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited = [0]*(N+1)

print(graph)
# print(visited)


def bfs(start_v):
    q = deque()
    q.append(start_v)
    visited[start_v] = 1
    count = 2
    while q:
        cur_v = q.popleft()
        for next_v in graph[cur_v]:
            if visited[next_v] == 0:
                q.append(next_v)
                visited[next_v] = count
                count += 1


bfs(R)

for i in visited[1::]:
    print(i)
