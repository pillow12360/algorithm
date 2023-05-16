def solution(n):
    answer = 0
    n = str(n)
    n = list(n)
    n.sort(reverse=True)
    n = list(map(int,n))
    
    for i,j in enumerate(n):
        a = j * 10 ** (len(n)-i-1)
        answer += a

    return answer

n = 123456

print(solution(n))

