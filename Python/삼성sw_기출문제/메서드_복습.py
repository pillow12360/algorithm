from collections import deque

text = "hello world python programming"
# 출력 예시: "Hello World Python Programming"

text = text.split(" ")

for i in text:
    i = i[0].upper()

print((" ").join(text))


#3번

text3 = "The quick brown fox jumps over the lazy dog"

dap3 = text3.split(" ")

print([i for i in dap3 if len(i) >= 3])





maze = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1]
]

def is_vaild(y,x,m,n):
    return 0 <= y < m and 0 <= x < n
def bfs(maze):
    dy = [1, -1, 0, 0]  # 위 아래 왼 오
    dx = [0, 0, -1, 1]

    n = len(maze) # 수직
    m = len(maze[0]) # 수평

    visited = [[-1] * m for _ in range(n)]

    q = deque([(0, 0)])
    visited[0][0] = 1

    while q:
        y,x = q.popleft()

        if x == m-1 and y == n-1:
            return visited[y][x]

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if is_vaild(next_y,next_x,n,m):
                if maze[next_y][next_x] == 1 and visited[next_y][next_x] == -1:
                    visited[next_y][next_x] = visited[y][x] + 1  # 거리 업데이트
                    q.append((next_y,next_x))

    return -1

print(bfs(maze))


