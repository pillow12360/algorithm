def solution(n, m):
    answer = []

    for i in range(min(m,n),0,-1):
        if n%i == 0 and m%i == 0:
            answer.append(i)
            break

    # for i in range():
    #   if n%i == 0 and m%i == 0:
    #       answer.append(i)
    #       break
    
    #실수 했던 코드 두수의 약수를 구하는 코드이므로 두수의 공통된 최대공약수가 아니다.


    if len(answer) == 0:
        answer.append(1)

    # 만일 최대공약수가 없으면 1을 push

    for i in range(max(n,m),(n*m)+1): # 두 수중 큰것 부터 두수의 곱까지 반복하다
        if  i%n == 0 and i%m == 0: # 처음으로 공배수를 찾으면 그 수는 최소공배수
            answer.append(i)
            break
        # 처음수를 찾고 다시 반복하지 않게 break문 사용
        
    return answer

print(solution(12,4))