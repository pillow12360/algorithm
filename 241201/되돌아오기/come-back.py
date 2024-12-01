from collections import deque

N = int(input())

q = deque()

for _ in range(N):
    q.append(list(input().split()))

mapper = {
    "W" : 0,
    "S" : 1,
    "N" : 2,
    "E" : 3
}

dr = [0,1,-1,0]
dc = [-1,0,0,1]

r, c = 0,0

def answer(r,c):
    time = 0

    while q:

        cur_d, dis = q.popleft()

        cur_d = mapper[cur_d]

        for i in range(int(dis)):
            time += 1
            r = r + dr[cur_d]
            c = c + dc[cur_d]

            if r == 0 and c == 0:

                return time
    
    return -1

print(answer(r,c))