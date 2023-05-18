def solution(x, n):
    answer = []
    a = x
    for i in range(0,n):
        answer.append(a)
        a += x
    return answer