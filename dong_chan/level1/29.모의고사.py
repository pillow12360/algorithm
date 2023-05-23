def solution(answers):
    answer = []

    Adap = 0
    Bdap = 0
    Cdap = 0

    A = [1,2,3,4,5]

    while(len(answers)>=len(A)):
       A *= 2

    for i in range(len(answers)):
      if A[i] == answers[i]:
         Adap += 1
  
    B = []
    while(len(answers) >= len(B)):
       for i in range(1,6):
          if i != 2:
            B.append(2)
            B.append(i)

    for i in range(len(answers)):
      if B[i] == answers[i]:
         Bdap += 1

    C1 = [3,1,2,4,5]
    C = []
    while (len(answers) >= len(C)):
       for i in C1:
          C.append(i)
          C.append(i)

    for i in range(len(answers)):
          if C[i] == answers[i]:
            Cdap += 1

    temps = []
    temps.append(Adap)
    temps.append(Bdap)
    temps.append(Cdap)

    maxvalue = max(temps)

    if Adap == maxvalue:
       answer.append(1)
    
    if Bdap == maxvalue:
       answer.append(2)
    
    if Cdap == maxvalue:
       answer.append(3)

       
    answer = sorted(answer)

    return answer

answers = [1,3,2,4,2]	

print(solution(answers))