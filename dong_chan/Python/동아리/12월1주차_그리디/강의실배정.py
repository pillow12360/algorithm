from heapq import heapify, heappop, heappush

# 12월 04일 골드5 그리디

# 강의실 배정

N = int(input())
time = []
for _ in range(N):
    time.append(list(map(int, input().split())))

heapify(time)

gang = 0
gang_list = []

for i in range(N):
    [a, b] = heappop(time)
    print(a, b)
