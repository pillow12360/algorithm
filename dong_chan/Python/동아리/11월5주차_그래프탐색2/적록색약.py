from collections import deque

N = int(input())

graph = [[] for _ in range(N)]

visited = [[False] * N for _ in range(N)]

for i in range(N):
    graph[i] = list(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

q = deque()

count = 0


def bfs(r, c, target):
    global count
    count += 1

    q.append((r, c))
    visited[r][c] = True

    while q:
        cur_r, cur_c = q.popleft()
        for i in range(4):
            next_r = cur_r + dy[i]
            next_c = cur_c + dx[i]

            if 0 <= next_r < N and 0 <= next_c < N:
                if graph[next_r][next_c] == target and not visited[next_r][next_c]:
                    q.append((next_r, next_c))
                    visited[next_r][next_c] = True
    return visited


def count_color(graph):

    for i in range(N):
        for j in range(N):
            if graph[i][j] == "R" and not visited[i][j]:
                target = "R"
                bfs(i, j, target)
            if graph[i][j] == "G" and not visited[i][j]:
                target = "G"
                bfs(i, j, target)
            if graph[i][j] == "B" and not visited[i][j]:
                target = "B"
                bfs(i, j, target)
            if graph[i][j] == "P" and not visited[i][j]:
                target = "P"
                bfs(i, j, target)

    return count


count_color(graph)

print(count, end=" ")

for i in range(N):
    for j in range(N):
        if graph[i][j] == "G" or graph[i][j] == "R":
            graph[i][j] = "P"
visited = [[False] * N for _ in range(N)]
count = 0
count_color(graph)


print(count)
