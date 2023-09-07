# 9월 4일 인프런 재귀

# 재귀의 구성요소 2가지

# 점화식
# 베이스 케이스
# 두 구성요소 모두 필수로 있어야 한다.

# 최종적으로 base case 를 이용하여 문제를 해결할 수 있어야함
# base case를 항상 염두하여 코드를 구성한다.

# 전체 시간 복잡도 = 재귀 함수 호출 수 x 재귀 함수 하나당 시간복잡도


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(4))
