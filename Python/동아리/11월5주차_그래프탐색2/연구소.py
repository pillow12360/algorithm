# 11_24 그래프 연구소 골드 4
# 답안 확인
from collections import deque
import copy

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]


dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]


def bfs():
    q = deque()

    test_graph = copy.deepcopy(graph)

    for i in range(N):
        for j in range(M):
            if test_graph[i][j] == 2:
                q.append((i, j))

    while q:
        cur_r, cur_c = q.popleft()

        for i in range(4):
            next_r = cur_r + dy[i]
            next_c = cur_c + dx[i]

            if 0 <= next_r < N and 0 <= next_c < M and test_graph[next_r][next_c] == 0:
                test_graph[next_r][next_c] = 2
                q.append((next_r, next_c))

    global result
    count = 0

    for i in range(N):
        for j in range(M):
            if test_graph[i][j] == 0:
                count += 1

    result = max(result, count)

# print(graph)


def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(count+1)
                graph[i][j] = 0


result = 0
make_wall(0)

print(result)
