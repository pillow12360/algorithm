import math

def solution(n):
    x = n**(1/2)

    if float(x).is_integer():
        answer = (x+1)**2
    else:
        answer = -1

    return answer

n = int(input())

print(solution(n))

