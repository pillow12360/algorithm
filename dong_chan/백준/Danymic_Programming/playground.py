'''

def sum_of_digits(n): # 0부터 n까지의 모든 합
    if n == 0:
        return 0
    else:
        dp = [0] * (n + 1) #구할 리스트의 요소 개수 만큼 0으로 초기화 
        dp[0] = 0 # 0인덱스는 0으로 초기화
        for i in range(1, n + 1): #1번째 인덱스 부터 구할 마지막 인덱스 까지 반복
            dp[i] = dp[i - 1] + i  # i인덱스는 전 인덱스와의 합
        return dp[n]

# print(sum_of_digits(10))

# def fibonacci(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci(n): # 피보나치 수열
    if n == 0 or n == 1: # 0과 1
        return n
    else:
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

print(fibonacci(10))

'''

#파이썬의 |= 연산자

# |와 |=는 dictionary, counter, number에 사용할 수 있다

a = {1,2,3,4}
b = {4,5,6}

a |= b
print(sorted(a))

# 다른 사람의 풀이
from itertools import permutations
def solution(n):
    a = set() # 중복을 제거하려 집합자료형으로 선언
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1)))) # 모든 경우의 수를 구하는 코드
    a -= set(range(0, 2)) #0과 1을 차집합으로 제거
    for i in range(2, int(max(a) ** 0.5) + 1): # 에라토스테네스의 체를 이용하여 소수 판별 후 제거
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

n = "011"
print(solution(n))