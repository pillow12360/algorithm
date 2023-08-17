# 8월10일 회의실 배정

# 8월 17일 회의실 배정

# 정렬까지 풀다가 로직 힌트 얻음

import sys
N = int(input())

tuple_a = []

while N > 0:
    a = tuple(int(x) for x in input().split())
    tuple_a.append(a)
    N -= 1

tuple_a.sort(key=lambda x: (x[1]))

answer = 0

if tuple_a[0][1] == tuple_a[1][1]:
    a = max(tuple[0][1], tuple[1][1])
else:
    a = tuple_a[0][1]

for i in range(len(tuple_a)):
    if a < tuple_a[i][0]:
        answer += 1
        a = tuple_a[i][1]

    elif a == tuple_a[i][0]:
        a = max(a, tuple[i][1])
        answer += 1

print(answer+1)

# 내가 푼 문제 but 런타임 에러 발생 (이유) (동작하는 로직은 같음)


N = int(sys.stdin.readline())

time = [[0]*2 for _ in range(N)]
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    time[i][0] = s
    time[i][1] = e

time.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end_time = time[0][1]
for i in range(1, N):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)
