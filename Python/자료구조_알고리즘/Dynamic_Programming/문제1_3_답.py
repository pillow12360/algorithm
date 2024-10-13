# 풀이3 색종이로 만들 수 있는 모든 조합을 만든 후 소수 인지 판별

import itertools
'''
numbers = "71"
numbers1 = [n for n in numbers] 
paper = [] # 색종이로 만들 모든 경우의 수 리스트
answer = []

for i in range(1,len(numbers)+1): # itertools 모듈을 사용하여 순열을 구하는 과정 모든 1자리수 부터 최대 자리수 까지 반복
    paper+=list(itertools.permutations(numbers1, i))
    List = [int(("").join(p)) for p in paper] #답안 확인함 https://dev-note-97.tistory.com/99

# 반환된 튜플을 int형으로 바꾸는 과정풀이 불가능

#List 소수 판별

for i in List:
    yack = []
    if i == 1:
        continue
    for j in range(2,i+1):
        if i % j == 0:
            yack.append(j)
    if len(yack) == 1: # 약수가 자기 자신 뿐이면 소수
        answer.append(i)

answer = len(set(answer))

print(answer)

# 30분 소요
'''

# 솔루션 함수로 바꾸어주었음
def solution(numbers):
    numbers1 = [n for n in numbers] 
    paper = [] # 색종이로 만들 모든 경우의 수 리스트
    answer = [] # 경우의 수 중 소수일 경우의 리스트

    for i in range(1,len(numbers)+1): # itertools 모듈을 사용하여 순열을 구하는 과정 모든 1자리수 부터 최대 자리수 까지 반복
        paper+=list(itertools.permutations(numbers1, i))
        #반환된 튜플의 값을 int형으로 바꾸는 방법을 생각하지 못함
        List = [int(("").join(p)) for p in paper] #★
        #답안 확인함 https://dev-note-97.tistory.com/99


    #List 소수 판별

    for i in List:
        yack = [] 
        if i == 1:
            continue
        for j in range(2,i+1):
            if i % j == 0:
                yack.append(j)
        if len(yack) == 1: # 약수가 자기 자신 뿐이면 소수
            answer.append(i)

    return len(set(answer))

numbers = '011'
print(solution(numbers))

# 총 약 2시간 50분 소요 

# 순열 : 순서를 고려하여 만들 수 있는 조합
# 조합 : 순서 상관없이 집합으로 만드는 조합 

#에라투스테네스의 체를 이용한 풀이 by chatgpt

import itertools

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return primes

def solution(numbers):
    numbers1 = list(numbers)
    paper = []  # 모든 가능한 순열의 리스트
    answer = []  # 소수의 리스트

    for i in range(1, len(numbers) + 1):
        paper += list(itertools.permutations(numbers1, i))
        num_list = [int("".join(p)) for p in paper]

    # 에라토스테네스의 체를 이용하여 소수 확인
    max_num = max(num_list)
    primes = sieve_of_eratosthenes(max_num)

    for num in num_list:
        if primes[num]:
            answer.append(num)

    return len(set(answer))


# 다른사람의 풀이
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

# 나의 풀이와 같은점 다른점
# 같은점
# itertools 사용 후 소수 판별하는 로직

# 다른점
# 집합과 차집합을 이용하여 간결한 풀이 사용
# 에라토스테네스의 체를 이용한 소수 판별후 바로 제거해주는 로직
# 메모리 사용량 및 실행시간의 상당한 이점