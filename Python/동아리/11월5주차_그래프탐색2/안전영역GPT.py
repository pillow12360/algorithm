from collections import deque


def bfs(graph, visited, start, threshold):
    n = len(graph)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > threshold:
                visited[nx][ny] = True
                queue.append((nx, ny))


def count_safe_areas(graph, max_height):
    n = len(graph)
    max_safe_area_count = 1  # 최소한 한 영역은 존재하므로 1로 초기화

    for threshold in range(1, max_height + 1):
        visited = [[False] * n for _ in range(n)]
        safe_area_count = 0

        for i in range(n):
            for j in range(n):
                if not visited[i][j] and graph[i][j] > threshold:
                    bfs(graph, visited, (i, j), threshold)
                    safe_area_count += 1

        max_safe_area_count = max(max_safe_area_count, safe_area_count)

    return max_safe_area_count


# 입력 예시
N = int(input())
height_map = [[]*N for _ in range(N)]

for i in range(N):
    height_map = map(int, input().split())

max_height = max(max(row) for row in height_map)
result = count_safe_areas(height_map, max_height)

print(result)
