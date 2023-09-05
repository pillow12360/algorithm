# 9월 4일 인프런 재귀

# 재귀의 구성요소 2가지

# 점화식
# 베이스 케이스

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(4))
