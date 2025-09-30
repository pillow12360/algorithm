
# grid = [
#     [1, 1, 1, 0, 1],
#     [0, 1, 0, 1, 1],
#     [1, 1, 1, 1, 0],
#     [0, 1, 0, 1, 1]
# ]

# # 맵의 크기
# N, M = len(grid), len(grid[0])

# # 방문 기록을 위한 2차원 visited 배열
# visited = [[False] * M for _ in range(N)]

# # 방향 벡터 (상, 하, 좌, 우)
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# def dfs_grid(r, c):
#     """격자(Grid)에서의 DFS 함수"""
#     # 1. 현재 위치 방문 처리
#     visited[r][c] = True
#     print(f"방문: ({r}, {c})")

#     # 2. 4방향의 이웃 노드(칸) 확인
#     for i in range(4):
#         nr = r + dr[i] # next row
#         nc = c + dc[i] # next column

#         # 3. 이웃이 유효한지 확인하는 조건들
#         # 조건 1: 맵의 경계를 벗어나지 않는가?
#         if 0 <= nr < N and 0 <= nc < M:
#             # 조건 2: 아직 방문하지 않았고, 이동 가능한 길(1)인가?
#             if not visited[nr][nc] and grid[nr][nc] == 1:
#                 # 4. 재귀 호출로 더 깊이 탐색
#                 dfs_grid(nr, nc)

# # 시작점 (0, 0)에서 DFS 실행
# dfs_grid(0, 0)



dr = [-1,1,0,0]
dc = [0,0,-1,1]

graph = [
    [1, 1, 1, 0, 1],
    [0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0],
    [0, 1, 0, 1, 1]
]

n = len(graph)
m = len(graph[0])
visited = [[False] * m for _ in range(n)]


def is_range(r,c):
    return 0<=r<n and 0<=c<m

def dfs (r, c):
    visited[r][c] = True
    print(r, c)
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]

        if is_range(nr,nc):
            if not visited[nr][nc] and graph[nr][nc] == 1:
                dfs(nr,nc)

def bfs(r,c):
    q = deque()
    q.append([r,c])
    visited[r][c] = True

    while q:
        c_r, c_c = q.popleft()
        
        for i in range(4):
            n_r = c_r + dr[i]
            n_c = c_c + dc[i]

            if is_range(n_r,n_c):
                if graph[n_r][n_c] == 1 and not visited[n_r][n_c]:
                    print(n_r, n_c)
                    q.append([n_r,n_c])
                    visited[n_r][n_c] = True

dfs(0,0)
