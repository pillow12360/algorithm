from collections import deque

maze = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1]
]

def bfs(maze):

    dy = [1,-1,0,0]
    dx = [0,0,-1,1]

    n = len(maze) # 수직 row
    m = len(maze[0]) # 수평 col

    visited = [[-1] * m for _ in range(n)]

    q = deque([(0,0)])
    visited[0][0] = 1

    while q:
        y, x = q.popleft()

        if x == m-1 and y == n-1:
            print(visited)
            return visited[y][x]

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < m and 0 <= ny < n:
                if visited[ny][nx] == -1 and maze[ny][nx] == 1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny,nx))
    return -1


print(bfs(maze))