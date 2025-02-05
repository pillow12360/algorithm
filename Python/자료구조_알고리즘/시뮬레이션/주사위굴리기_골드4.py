import sys

# 입력 받기
N, M, x, y, K = map(int, sys.stdin.readline().split())  # 지도 크기, 주사위 시작 좌표, 명령 개수
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 지도 정보
commands = list(map(int, sys.stdin.readline().split()))  # 이동 명령 리스트

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [0] * 6


def roll_dice(d):
    global dice
    if d == 1:  # 동쪽
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]
    elif d == 2:  # 서쪽
        dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]
    elif d == 3:  # 북쪽
        dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]
    elif d == 4:  # 남쪽
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]


for command in commands:

    nx, ny = x + dx[command - 1], y + dy[command - 1]

    if not (0 <= nx < N and 0 <= ny < M):
        continue

    x, y = nx, ny

    if not (0 <= x < N and 0 <= y < M):
        continue

    roll_dice(command)

    if board[x][y] == 0:
        board[x][y] = dice[1]
    else:
        dice[1] = board[x][y]
        board[x][y] = 0

    print(dice[0])
