n, m = map(int, input().split())

n+=1
grid = [[0]* n for _ in range(n) ]

def is_range(r,c):
    return 1<= r < n and 1 <= c < n
 
dr = [-1,0,1,0]
dc = [0,1,0,-1]

def is_com(r,c):

    grid[r][c] = 1

    cnt = 0

    for i in range(4):
        n_r = r + dr[i]
        n_c = c + dc[i]

        if is_range(n_r,n_c) and grid[n_r][n_c] == 1:
            cnt += 1  
    
    if cnt == 3:
        return 1


    return 0
    
for _ in range(m):
    r, c = map(int, input().split())
    print(is_com(r,c))
