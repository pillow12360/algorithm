# 1월 27일 시뮬레이션 2
# 톱니 바퀴 - 골드 5
# 오후 16시

# 예시 1번 톱니를 반시계 회전 -> 2번 톱니의 맞닿은 부분이 같은 극 : 2번이 시계 다른 극 : 반시계
# 총 4개의 톱니가 서로 맞물리며 회전하는 상황을 시뮬레이션

# 톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전

'''
총 K번 회전시킨 이후에 네 톱니바퀴의 점수의 합을 출력한다. 점수란 다음과 같이 계산한다.

1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점

12방향이 어떤 인덱스 값인지 알아야해

상태는 8개의 정수로 이루어져 있고, 12시방향부터 시계방향 순서대로 주어진다 -> 1번 인덱스 의 값 : 12시

방향 1 : 시계
방향 -1 : 반시계

N극 : 0
S극 : 1

'''

'''
덱 자료구조에 시계의 정보를 저장하여 rotate 메서드를 이용하여 톱니의 회전을 구현
rotate(1) 왼쪽 반시계
rotate(-1) 오른쪽 시계

맞닿은 극이 서로 다를때 -> 회전했던 톱니의 반대로 회전 함 
극이 서로 같을 때 -> 회전 x

1번 2번 서로 다른 극 -> 1번이 시계 2번 반시계, 1번 반시계 2번 시계

맞닿은 극

1번[2] 2번[6]
2번[2] 3번[6]
3번[2] 4번[6]

topni[0][2] , topni[1][6]
topni[1][2] , topni[2][6]
topni[2][2] , topni[3][6]

서로 비교

회전 로직 시계, 반시계

'''

'''
from collections import deque
topni = []

for _ in range(4):
    topni.append(deque((map(int, input()))))

print(topni)

n = int(input())

# 이런식으로 하나하나 조건을 다 하는 것 보다 효율적인 방법이 있을까?


def rotate_topni(t, d):  # t: 톱니 인덱스, d : 방향 시계 : 1시계 -1 반시계
    t -= 1  # 1번시계의 인덱스는 0
    if d == 1:
        topni[t].rotate(-1)
    else:
        topni[t].rotate(1)


def topni_search(i, d):  # i : 회전된 시게의 번째
    if i == 1:
        if topni[0][2] != topni[1][6]:
            if d == 1:
                rotate_topni(2, -1)
            else:
                rotate_topni(2, 1)

    if i == 2:
        if topni[0][2] != topni[1][6]:
            if d == 1:
                rotate_topni(2, -1)
            else:
                rotate_topni(2, 1)


for _ in range(n):
    t, d = map(int, input().split())
    rotate_topni(t, d)

# 처음 접근 풀이
# 먼저 문제에서 톱니를 회전 시킨 후 - 양옆 맞물려 있는 톱니 상태 확인 -> 로직대로 돌아가기 처리
# 문제 : 1번 은 2번 톱니와 맞물려있다.
    # 2번은 1번 3번과 맞물려있다. 즉 경우마다 전부 확인해야하는 문제 발생
'''


# 왼쪽에 있는 톱니들을 돌리기 + 오른쪽에 있는 톱니들을 돌리기

import sys
from collections import deque
input = sys.stdin.readline
t = [deque(list(map(int, input().rstrip()))) for _ in range(4)]  # 톱니 상태 저장

# 톱니 돌리기
k = int(input())
for _ in range(k):
    r = []  # 처음 톱니 상태 저장
    for i in range(4):
        r.append([t[i][6], t[i][2]])
    n, d = map(int, input().split())
    n = n-1

# 왼쪽에 있는 톱니들 회전
    if n != 0:  # 맨왼쪽에 있는 톱니가 아닐경우
        for i in range(n, 0, -1):  # 인덱스를 줄여나가며 진행
            if r[i][0] != r[i-1][1]:
                if (n-(i-1)) % 2 == 0:  # 따로 해석
                    t[i-1].rotate(d)
                elif (n-(i-1)) % 2 != 0:
                    t[i-1].rotate(-1*d)
            elif r[i][0] == r[i-1][1]:
                break

    # 오른쪽에 있는 톱니들 회전
    if n != 3:
        for i in range(n, 3):  # 왼쪽을 돌릴 때와 같은 로직으로
            if r[i][1] != r[i+1][0]:  # 맞물려있는 상태가 다른 경우에만
                if (n-(i+1)) % 2 == 0:
                    t[i+1].rotate(d)
                elif (n-(i+1)) % 2 != 0:
                    t[i+1].rotate(-1*d)
            elif r[i][1] == r[i+1][0]:
                break  # 연쇄작용이 일어나지 않게 종료
    t[n].rotate(d)

# 출력
res = 0
if t[0][0] == 1:
    res += 1
if t[1][0] == 1:
    res += 2
if t[2][0] == 1:
    res += 4
if t[3][0] == 1:
    res += 8
print(res)
