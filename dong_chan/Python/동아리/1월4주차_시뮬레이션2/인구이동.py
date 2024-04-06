# 1월 30일 화요일
# 인구 이동 시뮬레이션 2
# 골드 4
# 그래프
from collections import deque

N, L, R = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# print(graph)

q = deque()
united = []  # 국경이 합쳐지는 국가들을 저장하기 위한 리스트

dy = [-1, 1, 0, 0]  # 상 하 좌 우
dx = [0, 0, -1, 1]

oneday = []


def bfs(r, c, visited):
    if visited[r][c]:
        return False

    q = deque()
    q.append((r, c))
    visited[r][c] = True
    united = [(r, c)]
    hap = graph[r][c]
    count = 1
    while q:
        cur_r, cur_c = q.popleft()
        for i in range(4):
            next_r, next_c = cur_r + dy[i], cur_c + dx[i]
            # 인덱스 처리와 방문 여부
            if 0 <= next_r < N and 0 <= next_c < N and not visited[next_r][next_c]:
                if graph[cur_r][cur_c] >= graph[next_r][next_c]:
                    dif = graph[cur_r][cur_c] - graph[next_r][next_c]
                else:
                    dif = graph[next_r][next_c] - graph[cur_r][cur_c]
                if L <= dif <= R:
                    count += 1
                    visited[next_r][next_c] = True
                    hap += graph[next_r][next_c]
                    united.append((next_r, next_c))
                    q.append((next_r, next_c))
    if count > 1:
        avg = hap//count
        for i in united:
            graph[i[0]][i[1]] = avg
        return True
    return False


day = 0
while True:
    visited = [[False] * N for _ in range(N)]

    finish = True

    for i in range(N):
        for j in range(N):
            if bfs(i, j, visited):
                finish = False

    if finish:
        break
    day += 1

print(day)

# 키워드 : 그래프 탐색 : bfs
# 인접한 4 방향으로 탐색 후 ->
# 리스트에 l, r 사이를 만족하는 국가를 저장
# 저장 한 모든 국가의 평균 값을 계산 후 모든 국가에 저장

# 모두 찾아도 인구 이동이 없을 시 -> break
