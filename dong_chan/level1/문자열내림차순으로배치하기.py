def solution(s):
    answer = ''
    s = sorted(s,reverse=True)
    for i in s:
        answer += i
    
    return answer

# s = "Zbcdefg"

# print(solution(s))

s = "Zbcdefg"	

print(solution(s))