n, m = map(int, input().split())
s_r, s_c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

clean = 0  # 청소한 칸의 개수

# 북, 동, 남, 서 방향 정의
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def turn_left(d):
    return (d - 1) % 4  # 반시계 방향으로 회전


while True:
    if graph[s_r][s_c] == 0:  # 현재 칸을 청소
        graph[s_r][s_c] = 2
        clean += 1

    all_directions_checked = True
    for _ in range(4):  # 4 방향 모두 확인
        d = turn_left(d)
        nr, nc = s_r + dr[d], s_c + dc[d]
        if graph[nr][nc] == 0:  # 청소할 공간이 있는 경우
            s_r, s_c = nr, nc  # 전진
            all_directions_checked = False
            break  # 청소할 공간을 찾았으니 for문 탈출

    if all_directions_checked:  # 주변에 청소할 공간이 없는 경우
        nr, nc = s_r - dr[d], s_c - dc[d]  # 후진 기존 로직을 - 하는 것으로 구현
        if graph[nr][nc] == 1:  # 뒤쪽이 벽인 경우
            break  # 작동을 멈춤
        else:
            s_r, s_c = nr, nc  # 후진

print(clean)  # 청소한 칸의 개수 출력
