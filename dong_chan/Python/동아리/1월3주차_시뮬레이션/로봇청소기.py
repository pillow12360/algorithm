# 1월 18일
# 시뮬레이션 골드5

# 로봇 청소기

n, m = map(int, input().split())

# 로봇 청소기의 좌표

s_r, s_c, d = map(int, input().split())
# s : start 출발
# 방향 d : 0북 1동 2남 3서

# 2 : 벽

graph = []


for _ in range(m):
    graph.append(list(map(int, input().split())))

# print(graph)

clean = 0  # 답안 출력 변수 청소한 칸


def forward(r, c, d):  # d 방향으로 전진
    if d == 0:  # 북
        dr = -1
        dc = 0
        r += dr
        c += dc
    elif d == 1:  # 동
        dr = 0
        dc = 1
        r += dr
        c += dc
    elif d == 2:  # 남
        dr = 1
        dc = 0
        r += dr
        c += dc
    elif d == 3:  # 서
        dr = 0
        dc = -1
        r += dr
        c += dc
    return r, c


def backward(r, c, d):
    if d == 0:  # 북
        dr = 1
        dc = 0
        r += dr
        c += dc
    elif d == 1:  # 동
        dr = 0
        dc = -1
        r += dr
        c += dc
    elif d == 2:  # 남
        dr = -1
        dc = 0
        r -= dr
        c += dc
    elif d == 3:  # 서
        dr = 0
        dc = 1
        r += dr
        c += dc
    return r, c


def turn_d(d):  # 반시계로 90도 회전
    if d == 0:
        d = 3
    elif d == 1:
        d = 0
    if d == 2:
        d = 1
    if d == 3:
        d = 2
    return d


# 현재 로봇 위치
c_r = s_r + 1
c_c = s_c + 1

while True:

    if graph[c_r][c_c] == 0:
        graph[c_r][c_c] = 2
        clean += 1

    clean_check = True

    for i in range(4):  # 4칸 중 빈칸 있는 지 확인
        n_r, n_c = forward(c_r, c_c, i)
        if graph[n_r][n_c] == 0:
            clean_check = False
    # 청소 되지 않는 칸 이 있는 경우
    # 90 도 회전 : 북->서, 서->남, 남->동, 동->북

    if clean_check == False:
        for _ in range(4):
            turn_d(d)  # 90도 회전
            n_r, n_c = forward(c_r, c_c, d)
            if 0 <= n_r < n-1 and 0 <= n_c < m-1:
                if graph[n_r][n_c] == 0:
                    c_r, c_c = n_r, n_c  # 한칸 전진
                    continue
    else:  # 청소되지 않는 칸이 없는 경우 : 한칸 후진-> 1번 돌아가
        b_r, b_c = backward(c_r, c_c, d)
        if graph[b_r][b_c] == 1:  # 후진 후 벽이 있다면 끝
            break
        else:
            c_r, c_c = b_r, b_c  # 아니면 뒤로 후진

print(clean)
