def solution(n):
    answer = []
    
    n = str(n)
    m=[]

    for i in range(0,len(n)):
       m.append(n[i]) 

    for i in range(0,len(m)):
      answer.append(int(m.pop(-1)))

    return answer


print(solution(12345))
