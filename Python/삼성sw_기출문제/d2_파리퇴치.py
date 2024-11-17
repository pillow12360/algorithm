from collections import deque

def sum_fly(graph, y, x, m):
    fly = 0
    for i in range(y, y + m):
        for j in range(x, x + m):
            fly += graph[i][j]
    return fly


def bfs(graph, n, m):
    q = deque([(0, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True  # 시작점 방문 처리

    # 시작점의 파리 수를 최대값으로 초기화
    max_fly = sum_fly(graph, 0, 0, m)

    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            # M x M 크기의 파리채가 배열을 벗어나지 않는지 확인
            if 0 <= ny <= n - m and 0 <= nx <= n - m:
                if not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    # 현재 위치에서 파리의 수를 계산하고 최대값 갱신
                    cur_fly = sum_fly(graph, ny, nx, m)
                    max_fly = max(cur_fly, max_fly)

    return max_fly


T = int(input())  # 테스트 케이스 개수

for test_case in range(1, T + 1):
    n, m = map(int, input().split())

    # 그래프 입력 받기
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    result = bfs(graph, n, m)
    print(f'#{test_case} {result}')