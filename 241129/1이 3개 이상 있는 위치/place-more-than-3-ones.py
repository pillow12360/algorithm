n = int(input())

a = []

for _ in range(n):
    a.append(list(map(int, input().split())))

dxs, dys = [0,1,0,-1], [1,0,-1,0] # 상하좌우

def is_range(y,x):
    return 0<=y<n and 0<=x<n

def cnt_num(y, x):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        n_x = x + dx
        n_y = y + dy

        if is_range(n_y,n_x) and a[n_y][n_x]:
            cnt += 1

    if cnt >= 3:
        return True
    
    return False

answer = 0

for i in range(n):
    for j in range(n):
        
        if cnt_num(i,j):
            answer += 1

print(answer)