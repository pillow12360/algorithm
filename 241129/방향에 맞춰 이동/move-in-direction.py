from collections import deque

n = int(input())

dy = [0,1,-1,1]
dx = [-1,0,0,1]
# W S N E

q = deque()

for _ in range(n):
    q.append(list(input().split()))

cur_pos = [0,0]

while q:
    cur = q.popleft()

    if cur[0] == "W":
        cur_pos[1] += (dy[0] * int(cur[1]))
        cur_pos[0] += (dx[0] * int(cur[1]))
    elif cur[0] == "S":
        cur_pos[1] += (dy[1] * int(cur[1]))
        cur_pos[0] += (dx[1] * int(cur[1]))
    elif cur[0] == "N":
        cur_pos[1] += (dy[2] * int(cur[1]))
        cur_pos[0] += (dx[2] * int(cur[1]))
    elif cur[0] == "E":
        cur_pos[1] += (dy[3] * int(cur[1]))
        cur_pos[0] += (dx[3] * int(cur[1]))

cur_pos = map(str, cur_pos)

print(" ".join(cur_pos))