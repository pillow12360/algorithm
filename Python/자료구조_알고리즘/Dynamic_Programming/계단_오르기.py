# 0919 인프런 강의 숙제 

'''

당신은 계단을 오르고 있습니다. n정상에 도달하려면 단계가 필요합니다 .

매번 1개 또는 2개의 계단을 올라갈 수 있습니다. 얼마나 많은 방법으로 정상에 오를 수 있나요?

예시 1:

입력: n = 2
 출력: 2
 설명: 정상에 오르는 방법은 두 가지가 있습니다.
1. 1스텝 + 1스텝
2. 2단계

예 2:

입력: n = 3
 출력: 3
 설명: 정상에 오르는 방법에는 세 가지가 있습니다.
1. 1단계 + 1단계 + 1단계
2. 1단계 + 2단계
3. 2단계 + 1단계
 

제약:

1 <= n <= 45

'''

n = 2

memo = {1 : 1 , 2 : 2 , 3 : 3}


# 바로 구현이 생각나지 않는다.

'''
n이 5일 때를 생각해보자

생각해야 하는 경우의 수가 너무 많다.

완전 탐색을 재귀를 활용하여 푼다.

처음부터 완전 탐색을 이용하지 않는다면, 바로 생각해내기 쉽지 않다.

5층입장에서는 4층에서 오거나
3층에서 오는 방법만이 존재한다.
파악 중요

4층 까지 올라오는 경우의 수와
3층 까지 올라오는 경우의 수를 더하면 5층으로 갈 수 있는 경우의 수 이다.

하위 문제에 대한 답으로 원래 문제의 대한 답을 계산

'''

# top - down 방식 재귀 사용

memo = {}

def stair (n):
  if n == 1:
    return 1
  if n == 2:
    return 2
  # 간단한 하위 문제를 basecase로 지정

  if n not in memo:
    memo[n] = stair(n-1) + stair(n-2)

  return memo[n]

# bottom - up 방식 반복문 사용
# dp table
# tablation

memo = {1:1,2:2,3:3}

def stair(n):
  for i in range(3,n+1):
    memo[i] = memo[i-2] + memo[i-1]
  return memo[n]
