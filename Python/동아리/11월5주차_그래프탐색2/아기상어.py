# 11월 29일 수요일 아기 상어 (골드 3)
# 답안 확인

from collections import deque

N = int(input())

sea = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

position = []

for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            position.append(i)
            position.append(j)
# 아기 상어의 위치를 포지션 리스트에 저장

cnt = 0


def bfs(x, y):

    visited = [[0]*N for _ in range(N)]
    queue = deque([[x, y]])
    cand = []

    visited[x][y] = 1

    while queue:
        i, j = queue.popleft()

        for idx in range(4):
            ii, jj = i + dx[idx], j + dy[idx]

            if 0 <= ii and ii < N and 0 <= jj and jj < N and visited[ii][jj] == 0:
                # 다음 위치의 먹이가 있고 # 상어의 크기보다 먹이가 작은 경우라면
                if sea[x][y] > sea[ii][jj] and sea[ii][jj] != 0:
                    visited[ii][jj] = visited[i][j] + 1  # 방문 표시
                    cand.append((visited[ii][jj] - 1, ii, jj))  # 후보 리스트에 추가
                elif sea[x][y] == sea[ii][jj]:
                    visited[ii][jj] = visited[i][j] + 1
                    queue.append([ii, jj])  # 모든 인접한 경우를 따지기 위해 q에 append
                elif sea[ii][jj] == 0:
                    visited[ii][jj] = visited[i][j] + 1
                    queue.append([ii, jj])

    return sorted(cand, key=lambda x: (x[0], x[1], x[2]))


i, j = position

size = [2, 0]
# 0번인덱스 : 다음 크기
# 1번 인덱스 : 먹은 물고기 합

while True:
    sea[i][j] = size[0]  # 아기 상어의 위치를 상어의 크기로 바꾸어줌
    # why? 상어의 크기로 다음의 먹이를 먹어야 하는 if문에서 활용하기 때문

    cand = deque(bfs(i, j))  # bfs함수를 돌며 후보리스트 cand 반환
    # 후보는 오름차순 정렬 되어 있기 때문에 popleft 사용을 위한 deque 이용

    if not cand:  # 먹을 먹이후보가 없다면 = 엄마상어 호출
        break

    step, xx, yy = cand.popleft()  # 정렬된 후보 순서대로 변수 사용
    cnt += step
    size[1] += 1  # 물고기의 크기는 상관없이 횟수만 따짐

    if size[0] == size[1]:  # 자신의 크기와 먹은 물고기 횟수가 같다면
        size[0] += 1  # 자신의 크기를 늘리고
        size[1] = 0  # 먹은 물고리를 0으로 초기화

    sea[i][j] = 0  # 먹이를 먹었으니 빈 바다가 되고
    i, j = xx, yy  # 현재 위치 업데이트 하며 while문 반복

print(cnt)
