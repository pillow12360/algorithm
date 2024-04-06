from collections import deque


def solution(n, computers):
    # n 컴퓨터 개수
    # computers 연결 정보 그래프
    answer = 0
    visited = [[False] * n for _ in range(n)]  # 방문표시

    dc = [0, 0, -1, 1]
    dr = [1, -1, 0, 0]  # 상하좌우

    def bfs(c, r):
        q = deque()
        q.append((c, r))
        visited[c][r] = True

        while q:
            c, r = q.popleft()
            for i in range(4):
                nc = c+dc[i]
                nr = r+dr[i]
                if 0 <= nc < n and 0 <= nr < n and not visited[nc][nr]:
                    if computers[nc][nr] == 1:
                        visited[nc][nr] = True
                        q.append((nc, nr))

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and not visited[i][j]:
                answer += 1
                bfs(i, j)

    # print(visited)

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))
