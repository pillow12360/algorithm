from collections import deque

n = deque(list(input()))

# 처음 북쪽
cur_d = 0

dy = [1,0,-1,0] # 북 동 남 서
dx = [0,1,0,-1]

y,x = 0,0

time = 0
is_answer = False

while n:
    time += 1
    command = n.popleft()

    if command == "R":
        cur_d = (cur_d + 1) % 4
        continue
    elif command == "L":
        cur_d = (cur_d + 3) % 4
        continue
    else:
        y = y + dy[cur_d]
        x = x + dx[cur_d]

        if x == 0 and y == 0:
            is_answer = True
            break

if is_answer:
    print(time)
else:
    print(-1)

