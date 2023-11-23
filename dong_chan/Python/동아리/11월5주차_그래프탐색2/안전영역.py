from collections import deque

# 11월 23월 실버1 안전 영역

# 2차원 정사각형 N x N 에서 일정 높이 이상인 구역의 갯수를 구하는 문제

# 비가 1만큼 내린 경우부터 비가 최대 -1 로 내린 경우 까지 모든 경우의 수 구하기
# 모든 경우의 수 중에서 잠기지 않은 구역의 최대 갯수를 구하기

from collections import deque

N = int(input())

#  2<= N <= 100

graph = [[] for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, input().split()))

max_higher = max(map(max, graph))
# 최소 잠기는 높이와 최대 잠기는 높이

dap = []


def number_of_raniny(min_higher):
    number_of_raniny = 0
    row = N
    col = N
    visited = [[False] * col for _ in range(row)]

    def bfs(r, c):

        dx = [0, 0, -1, 1]  # 상, 하, 좌,우
        dy = [1, -1, 0, 0]

        visited[r][c] = True
        queue = deque()
        queue.append((r, c))

        while queue:
            cur_y, cur_x = queue.popleft()
            for i in range(4):
                next_y = cur_y + dx[i]
                next_x = cur_x + dy[i]
                if 0 <= next_y < row and 0 <= next_x < col:  # 탐색 범위 제한
                    if graph[next_y][next_x] > min_higher and not visited[next_y][next_x]:  # 잠기지 않은 높이만 탐색
                        visited[next_y][next_x] = True
                        queue.append((next_y, next_x))
        return visited

    for r in range(row):
        for c in range(col):
            # 잠기지 않은 높이 and 탐색하지 않은 높이만 탐색 시작
            if N > 2 and graph[r][c] > min_higher and not visited[r][c]:
                bfs(r, c)  # 탐색 시작
                number_of_raniny += 1
            if N == 2:
                return 1
    return number_of_raniny


for i in range(0, max_higher):
    dap.append(number_of_raniny(i))

# print(dap)
if dap:
    print(max(dap))
else:
    print(0)


'''
from collections import deque

N = int(input())

graph = [[] for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, input().split()))

max_higher = max(max(row) for row in graph)
dap = []


def number_of_rainy(min_higher):
    number_of_rainy = 0
    row = N
    col = N
    visited = [[False] * col for _ in range(row)]

    def bfs(r, c):
        dx = [0, 0, -1, 1]  # 상, 하, 좌,우
        dy = [1, -1, 0, 0]

        visited[r][c] = True
        queue = deque()
        queue.append((r, c))

        while queue:
            cur_y, cur_x = queue.popleft()
            for i in range(4):
                next_y = cur_y + dy[i]
                next_x = cur_x + dx[i]
                if 0 <= next_y < row and 0 <= next_x < col and graph[next_y][next_x] > min_higher and not visited[next_y][next_x]:
                    visited[next_y][next_x] = True
                    queue.append((next_y, next_x))

    for r in range(row):
        for c in range(col):
            if graph[r][c] > min_higher and not visited[r][c]:
                bfs(r, c)
                number_of_rainy += 1

    return number_of_rainy


for i in range(1, max_higher + 1):
    dap.append(number_of_rainy(i))

print(max(dap))
'''


N = int(input())
max_higher = 0

graph = [[] for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, input().split()))
    for j in range(N):
        if graph[i][j] > max_higher:
            max_higher = graph[i][j]

max_higher = max(max(graph))
dap = []

dx = [0, 0, -1, 1]  # 상, 하, 좌,우
dy = [1, -1, 0, 0]


def bfs(r, c, min_higher, visited):

    visited[r][c] = True
    queue = deque()
    queue.append((r, c))

    while queue:
        cur_y, cur_x = queue.popleft()
        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            if 0 <= next_y < N and 0 <= next_x < N:  # 탐색 범위 제한
                if graph[next_y][next_x] > min_higher and not visited[next_y][next_x]:  # 잠기지 않은 높이만 탐색
                    visited[next_y][next_x] = True
                    queue.append((next_y, next_x))


result = 0

for i in range(max_higher):
    visited = [[0] * N for i in range(N)]
    cnt = 0

    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i, visited)
                cnt += 1
    if result < cnt:
        result = cnt

print(result)
