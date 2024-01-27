# 1월 19일 금요일
# 골드 4
# 시뮬레이션
# 뱀

# 뱀이 벽 또는 자기 자신과 부딪히면 게임 종료
# 몇초에 종료되는가??
# 초마다 이동 -> 이동한 칸 이 곧 걸린 시간

# 몸 한칸 이동
# 벽 또는 자기자신 부딪힘 해당 인덱스의 값이 벽또는 자기 몸이면 게임 끝
# 사과일 경우 꼬리 이동 x
# 사과가 없으면 앞으로 한칸 이동 몸길이 동일

from collections import deque
n = int(input())  # 보드의 크기 n x n

# 0 빈공간
# 1 벽
# 2 사과

board = []
for i in range(n):
    board.append([0]*n)

k = int(input())  # k : 사과 개수

apple = []
# 사과 위치 정보
for _ in range(k):
    apple_r, apple_c = map(int, input().split())
    apple_r, apple_c = apple_r - 1, apple_c - 1  # 인덱스 값으로 변경
    board[apple_r][apple_c] = 2
    apple.append((apple_r, apple_c))


l = int(input())  # 방향 정보 개수

change_snake = []

# dis : 시간 direct : 방향 전환
for _ in range(l):
    dis, direct = input().split()
    dis = int(dis)
    change_snake.append((dis, direct))

change_snake.append((10001, ''))
# 뱀의 몸 : 뱀의 이동 경로와 뱀의 길이


# 뱀의 방향 변환 정보
change = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# 방향 전환 함수
# 0 : 서 1 : 동 2 : 남 3: 북
# 인덱스와 순서를 활용하여 방향전환을 구현

# 처음시작시 동쪽으로 이동


def turn(direct):
    global turn_index
    if direct == 'L':
        if turn_index != 0:
            turn_index -= 1
        else:
            turn_index = 3
    else:
        if turn_index != 3:
            turn_index += 1
        else:
            turn_index = 0
    return
# 힌트 : 덱, 큐, 자료구조


snake = deque()
snake.append((0, 0))

turn_index = 1

# 뱀의 머리 위치
x, y = 0, 0
# 게임 진행 시간
cnt = 0
# 방향을 바꿀 때 출발 시간
start = 1

breaker = False

for i in range(len(change_snake)):
    start = cnt + 1
    # 다음 위치 변환 정보가 올때까지 방향전환 없이 계속 앞으로 전진
    for _ in range(start, change_snake[i][0]+1):
        nx = x + change[turn_index][0]  # 해당 방향을 설정하는 로직
        ny = y + change[turn_index][1]

        # 스네이크 몸에 부딪힐 경우 처리 방법
        if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in snake:
            cnt += 1
            breaker = True
            break
        if board[nx][ny] == 2:  # 사과라면
            board[nx][ny] = 0  # 사과를 먹어
            x, y = nx, ny  # 머리 위치 업데이트
            snake.append((x, y))  # 뱀의 머리 추가
        else:
            x, y = nx, ny  # 머리 위치 업데이트
            snake.popleft()  # 덱 구조 핵심 = 꼬리를 없애준다
            snake.append((x, y))  # 뱀의 머리 앞으로 이동
        cnt += 1
    if breaker == True:
        break
    turn(change_snake[i][1])

print(cnt)

# 뱀의 몸의 정보를 덱 자료구조로 저장하는 형식 => 전진했을 겨우 in 연산으로 부딪힐때 여부 처리

# 2차원 리스트에 표시하지 않아도 됨

# 사과를 먹지 않는 경우 popleft() 를 통해 뱀의 꼬리 부분을 삭제 + 뱀의 머리의 정보를 append()

# 사과를 먹는 경우 -> 뱀의 머리에 대한 정보를 append()

# [(),(),(),()]
# 0번 인덱스 좌표값 -> 뱀의 마지막 꼬리 부분
# 마지막 인덱스 좌표값 -> 뱀의 머리 부분
