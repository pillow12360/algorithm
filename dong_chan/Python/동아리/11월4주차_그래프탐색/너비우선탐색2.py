from collections import deque

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort(reverse=True)

# print(graph)

visited = [0] * (N+1)


def bfs(start_v):
    global count
    visited[start_v] = count
    count += 1
    q = deque()
    q.append(start_v)

    while q:
        cur_v = q.popleft()
        for next_v in graph[cur_v]:
            if visited[next_v] == 0:
                visited[next_v] = count
                count += 1
                q.append(next_v)


count = 1
bfs(R)

for i in visited[1::]:
    print(i)
