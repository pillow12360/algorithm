# 0919 화요일 인프런 DP 개요

# 문제에 대한 정답이 될 가능성이 있는 모든 해결책을 "체계적"이고 "효율적"으로 탐색하는 풀이법

# 모든 해결책을 탐색하는 풀이 = 완전탐색 

# 완전탐색은 체계 x 효율 x 

# 완전 탐색에서 진화한 결과


# 1. 크고 복잡한 문제를 작은 문제로 나눈다. (subproblem - 하위문제)

# 2. 하위 문제의 답을 계산한다.
# 여기서 중복 계산해야 하는 하위 문제가 있다. (overlapping subproblem)

# 한번 계산한 결과는 메모리에 저장하여 재계산 하지 않도록 한다.

# 하위 문제에 대한 답을 통해 원래 문제에 대한 답을 계산 (optimal substructure - 최적 부분 구조)

# 예시문제 피보나치 수열

# 1. 완전탐색 (재귀)

# n-2 번째 n -1 번째 n 번째의 관계식을 : recurrence relation

# def fibo(n):
#   if n == 1 or n==2:
#     return 1
#   return fibo(n-2) + fibo(n-1)

# print(fibo(8))


'''
dp는 문제를 많이 풀어보는 것이 다른 알고리즘 보다 중요함

1. Overlapping subproblem
2. Optimal substructure

풀 수 있을 정도의 단순하게 subproblem 으로 나누고
중복되는 서브문제들을 재사용 하며 큰 problem을 푸는 방식

2. subproblem의 최적 해법으로 원래 문제의 최적 해법을 구할 수 있다.

top - down 
재귀 memoization

bottom - up
반복문 dp table

시작은 완전탐색 -> 재귀(반복문) -> 중복 재활용 -> dp 

메모리를 사용하여 시간복잡도를 낮추는 방법

문제를 보고 dp를 활용할 수 있는 문제인지 파악하는 방법

1. Optimum value (최대 ,최소), 방법의 개수 구하기

- 의 최소 비용, 최대 이익, 방법의 개수, 특정 지점에 도달 할 수 있는가

2. 미래의 계산이 앞선 계산 결과에 영향을 받을 때

(분할 정복: 퀵정렬, 병합정렬 )


구현에 꼭 필요한 두가지

recurrence relation - 점화식

대부분 문제에서 답이 있다. 문제에서 뽑아 낼 수 있는 능력은 연습만이 답이다.


base case - 베이스 케이스

관계식으로 답을 도출 해내지 않아도 바로 답을 도출 해 낼 수 있는 케이스


--------------------------------------------------------------------
bottom - up 방식 장단점

반복문 사용 -> 실행시간이 빠름

더 작은 subproblem에 대한 계산 결과를 DP table에 저장하여 더 큰 문제의 계산에 활용

hashtalbe 또는 list에 계산 결과 저장

top - down 방식

재귀 사용 -> 구현 시간이 빠르다. 

재귀풀이에서 중복되는 계산값을 저장하여 동일한 함수 호출 시 재활용 한다.

hash table 또는 list에 계산 결과를 저장



top - down 방식으로 구현 했을 때 실행시간이 길다면 bottom up 방식으로 변환 할 때도 많다.








'''
# dp 

# top - down 방식
memo = {}
def fibonazzi(n):
  if n == 1 or n == 2:
    return 1
  if n not in memo:
    memo[n] = fibonazzi(n-2) + fibonazzi(n-1)
  return memo[n]

print(fibonazzi(7))

# bottom - up 방식

def fibonazzi1(n):
  dp_table = [0]*n
  dp_table[0] = 1
  dp_table[1] = 1

  for i in range(2,n):
    dp_table[i] = dp_table[i-2] + dp_table[i-1]
  return dp_table[-1]

print(fibonazzi1(7))