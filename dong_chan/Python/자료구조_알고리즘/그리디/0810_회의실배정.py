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

# 회의가 끝나는 시간을 기준으로 정렬한다.
# 만약 끝나는 시간이 같을 경우, 시작 시간더 늦는 시간을 사용 한다.
# 끝나는 시간을 기준으로 시작 시간이 같거나 더 늦는 회의만을 골라 카운트를 센다.

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

# 구현의 문제 보다 간단하게 풀 수 있는 방법을 생각해 내는 것
#
# 내가 푼 문제 but 런타임 에러 발생 (이유는 찾지 못함) (동작하는 로직은 같음)


N = int(sys.stdin.readline())

time = [[0]*2 for _ in range(N)]  # 먼저 리스트를 초기화 한뒤
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    time[i][0] = s
    time[i][1] = e
# 입력값을 리스트에 저장한다.


time.sort(key=lambda x: (x[1], x[0]))
# 저장한 리스트를 x의 [1번째 인덱스를] 기준으로 정렬하고 , 같을 경우 0번째를 기준으로 정렬

cnt = 1

end_time = time[0][1]
# 처음 값을 지정해주고

for i in range(1, N):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)