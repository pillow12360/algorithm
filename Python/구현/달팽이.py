n = int(input())
num = int(input())

grid = [[0] * n for _ in range(n)]

def is_range(r,c):
    return 0 <= r < n and 0 <= c < n

dr = [1,0,-1,0]
dc = [0,1,0,-1]

cur_num = n * n

# n은 항상 홀수
c_r, c_c = 0, 0

cur_d = 0

grid[c_r][c_c] = cur_num
if num == n * n:
    a_r, a_c = 0,0

while cur_num > 0:
    if cur_num <= 1:
        break

    n_r = c_r + dr[cur_d]
    n_c = c_c + dc[cur_d]

    if is_range(n_r, n_c) and grid[n_r][n_c] == 0:
            cur_num -= 1
            grid[n_r][n_c] = cur_num
            if cur_num == num:
                a_r, a_c = n_r, n_c

            c_r = n_r
            c_c = n_c

    else:
        cur_d = (cur_d + 1) % 4

for i in grid:
    print(" ".join(map(str, i)))

a_r += 1
a_c += 1

print(a_r, a_c)