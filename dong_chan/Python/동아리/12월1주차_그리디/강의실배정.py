# 12월 7일 목요일
# 골드 5 그리디
# 우선순위 큐
# 정렬 sorted
# heap 힙

import heapq

N = int(input())

time = []

for _ in range(N):
    time.append(list(map(int, input().split())))

time = sorted(time)

room = []  # 배정된 강의실

heapq.heappush(room, time[0][1])  # 처음 강의의 끝나는 시간을 우선순위 큐에 저장

for i in range(1, N):  # 두번째 강의부터 시작
    if time[i][0] < room[0]:  # 현재 강의실의 끝나는 시간보다. 다음 회의 시작시간이 빠르면,
        heapq.heappush(room, time[i][1])
    else:
        heapq.heappop(room)  # 기존의 강의를 대체하고 새로운 강의로 끝나는 시간 변경을 휘해 pop후
        heapq.heappush(room, time[i][1])  # push 끝나는 시간을 푸쉬

print(len(room))  # 결론적으로 힙에 남아 있는 시간은 배정된 강의실에서 가장 늦게 끝나는 시간이 남는다.
