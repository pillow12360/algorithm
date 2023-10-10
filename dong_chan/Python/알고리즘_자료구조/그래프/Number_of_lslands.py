# 코테 적용 1 그래프

# grid는 1 과 0 으로 이루어진 지도를 표현하는 m x n 이차원 배열이다. 지도에 표시된 섬들의 총 개수를 반환하시오. 섬이란, 수평과 수직으로 연결되어 있고 주변은 물로 둘러 쌓여 있는 것을 말한다.

from collections import deque
grid = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]

# 대각선은 연결되어 있는것이 아니다.
# 다른 문제에서는 대각선도 연결 한 것일 수 있다 = 수정 필요

# 직관으로 이해가 되지 않는다면, '단순화, 극한화'를 해본다.
# 웬만한 문제들은 직관으로 풀 수 있다.

# 이 문제는 bfs, dfs 의 기본 문제이다. 외우기

# 모든 벌텍스에서 bfs를 시도 한다. 그리고 카운터를 하나 센다
# 하지만 이미 visited 된 벌텍스는 탐색 시도 제외

# BFS 코드 설계


def lsland(grid):

    number_of_islands = 0

    m = len(grid)
    n = len(grid[0])

    # 기억하기 색칠한다는 느낌 False -> True 색칠했다.
    visited = [[False]*n for _ in range(m)]

    def bfs(x, y):

        dx = [-1, 1, 0, 0]  # 상하좌우 구현
        dy = [0, 0, -1, 1]  # 암시적 그래프 이기 때문에

        visited[x][y] = True
        queue = deque()
        queue.append((x, y))
        while queue:
            cur_x, cur_y = queue.popleft()
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n:
                    if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                        # grid의 범위 (x,y), 섬일때, 방문안했을 때 만 방문
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))
        return visited

    for i in range(m):
        for j in range(n):

            if grid[i][j] == "1" and not visited[i][j]:
                bfs(i, j)
                number_of_islands += 1

    return number_of_islands


print(lsland(grid))


def number_of_island(grid):
    number_of_island = 0
    row = len(grid)
    col = len(grid[0])

    visited = [[False]*col for _ in range(row)]

    def bfs(r, c):

        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]

        visited[r][c] = True
        queue = deque()
        queue.append((r, c))

        while queue:
            cur_x, cur_y = queue.popleft()

            for i in range(4):
                next_x = cur_x+dx[i]
                next_y = cur_y+dy[i]

                if next_x >= 0 and next_x > col and next_y >= 0 and next_y < row:
                    if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))
        return visited

    for r in row:
        for c in col:
            if grid[r][c] == "1" and not visited[r][c]:
                bfs(r, c)
                number_of_island += 1

    return number_of_island


print(number_of_island(grid))


