from collections import deque

q = deque(list(input()))

# 시작 방향은 북
# 시계방향
# 0북 1동 2남 3서

cur_dir = 0
pos = [0,0]

dy = [-1,0,1,0]
dx = [0,1,0,-1]


while q:
    cur = q.popleft()

    if cur == "L":
        cur_dir = (cur_dir + 3) % 4
    elif cur == "R":
        cur_dir = (cur_dir + 1) % 4
    elif cur == "F":
        pos[1] += dy[cur_dir] 
        pos[0] += dx[cur_dir]
        
pos = map(str, pos)

print(" ".join(pos))