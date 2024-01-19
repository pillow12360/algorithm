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

n = int(input())  # 보드의 크기 n x n

# 0 빈공간
# 1 벽
# 2 사과

bode = [1] * (n+2)  # 상 벽

for i in range(n):
    bode.append([1]+[0]*n+[1])

bode.append([1]*(n+2))  # 하 벽

# print(bode)


k = int(input())  # k : 사과 개수

apple = []  # 사과 위치 정보
for _ in range(k):
    apple.append(list(map(int, input().split())))

# 뱀의 방향 변환 정보

l = int(input())  # 방향 정보 개수

info = []

for _ in range(l):
    info.append(input().split())

# 뱀의 몸 : 뱀의 이동 경로와 뱀의 길이

# 뱀의 길이
bam = 1


# 방향 전환

# 힌트 : 덱, 큐, 자료구조
