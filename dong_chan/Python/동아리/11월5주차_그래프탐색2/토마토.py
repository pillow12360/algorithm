from collections import deque

M, N = map(int, input().split())

box = [[]*M for _ in range(N)]

for r in range(N):
    box[r] = list(map(int, input().split()))

days = 0

# print(box)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

q = deque()

for r in range(N):
    for c in range(M):
        if box[r][c] == 1:
            q.append((r, c))
# 시작 지점 모두 큐에 추가


def bfs():
    while q:
        cur_r, cur_c = q.popleft()

        for i in range(4):
            next_r = cur_r + dx[i]
            next_c = cur_c + dy[i]
            if 0 <= next_c < M and 0 <= next_r < N and box[next_r][next_c] == 0:
                box[next_r][next_c] = box[cur_r][cur_c] + 1
                q.append((next_r, next_c))


bfs()
print(box)

for i in box:
    for j in i:
        if j == 0: # 0 값이 있을 경우 
            print(-1)
            exit(0)
    days = max(days, max(i))

print(days-1)
