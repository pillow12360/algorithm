n, t = map(int,input().split())

r, c, d = input().split()

dr, dc = [0,-1,1,0], [1,0,0,-1]

mapper = {
    "R" : 0,
    "U" : 1,
    "D" : 2,
    "L" : 3,
}

def is_range(r,c):
    return 1 <= r <= n and 1 <= c <= n

cur_d = mapper[d]

r = int(r)
c = int(c)

while t > 0:
    t -= 1

    n_r = r + dr[cur_d]
    n_c = c + dc[cur_d]

    if not is_range(n_r, n_c):
        cur_d = 3 - cur_d
        
        continue
    else:
        r = n_r
        c = n_c

print(f"{r} {c}")