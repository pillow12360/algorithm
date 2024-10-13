# 0915 백준문제 섬 아일랜드 백준 버전

from collections import deque

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    island = []

    for i in range(h):
        a = list(input().split())
        island.append(a)

    print(island)

    # print(island)

    # 섬의 개수를 구하라

    # bfs 방법

    # def bfs(graph, start_v):
    #   visited = [start_v]
    #   queue = deque(start_v)

    #   while queue:
    #     cur_v = queue.popleft()
    #     for v in graph[cur_v]:
    #       if v not in visited:
    #         queue.append(v)
    #         visited.append(v)
    #   return visited

    def Number_of_Island(grid):

        Number_of_Island = 0

        row = len(grid)  # 열
        col = len(grid[0])  # 행

        visited = [[False] * col for _ in range(row)]

        def BFS(r, c):
            dx = [1, -1, 0, 0, 1, -1, -1, 1]  # 상, 하, 좌,우, 대각선
            dy = [0, 0, -1, 1, 1, -1, 1, -1]

            grid[r][c] = True
            queue = deque()
            queue.append((r, c))

            while queue:
                cur_y, cur_x = queue.popleft()
                for i in range(8):
                    next_y = cur_y + dx[i]
                    next_x = cur_x + dy[i]
                    if next_y >= 0 and next_y < row and next_x >= 0 and next_x < col:
                        if grid[next_y][next_x] == "1" and not visited[next_y][next_x]:

                            visited[next_y][next_x] = True
                            queue.append((next_y, next_x))

            return visited

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and not visited[r][c]:
                    BFS(r, c)
                    Number_of_Island += 1

        return Number_of_Island


print(Number_of_Island(island))
