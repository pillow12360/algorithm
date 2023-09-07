# 9월 7일 목요일 백준 피보나치수5 브론즈2

N = int(input())


def fibonazzi(N):
    if N <= 1:
        return N
    return fibonazzi(N-2) + fibonazzi(N-1)


print(fibonazzi(N))
