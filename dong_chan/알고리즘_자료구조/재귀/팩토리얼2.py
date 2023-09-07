# 9월 7일 목 백준 팩토리얼2 브론즈5

N = int(input())


def factorial(N):
    if N == 0:
        return 1
    if N == 1:
        return 1
    return N*factorial(N-1)


print(factorial(N))
