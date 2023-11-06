# 08월 16일  18시 50분 그리디 실버 3

# 가장 적은 비용으로 도착하기

# 비싼 곳에는 최소한만 사고 가장 싼데에서 최대한 많이 주유해야함

from sys import stdin
N = int(input())

range = list(map(int, input().split()))

cost = list(map(int, input().split()))

hap = 0

cost.pop()
min_cost = min(cost)

for i, j in enumerate(cost):
    if j == min_cost:
        hap += sum(range[i:])*j
        break
    else:
        hap += range[i]*j

print(hap)

# 나의 풀이

# 답 확인


k = int(stdin.readline())
dist = list(map(int, stdin.readline().split()))
cost = list(map(int, stdin.readline().split()))
res = 0

c = cost[0]
for i in range(k - 1):
    if c > cost[i]:
        c = cost[i]
    res += c * dist[i]

print(res)
