n, m  = map(int, input().split())

answer = [[0] * m for _ in range(n)]

answer[0][0] = 1
cur_num = 2

r, c = 0,0

dr, dc = [0,-1,1,0],[1,0,0,-1]
cur_d = 0

def is_range(r,c):
    return 0<=r<n and 0<=c<m

while True:
    if cur_num > n * m:
        break

    n_r = r + dr[cur_d]
    n_c = c + dc[cur_d]

    if is_range(n_r,n_c) and answer[n_r][n_c] == 0:
        answer[n_r][n_c] = cur_num
        cur_num += 1
        r = n_r
        c = n_c
    else:
        cur_d = (cur_d + 1) % 4

for i in answer:
    print(" ".join(map(str,i)))
