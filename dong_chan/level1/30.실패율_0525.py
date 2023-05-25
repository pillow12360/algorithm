from collections import Counter

def solution(N, stages):
    answer=[]
    chamga = len(stages) #참가한 사람 수
    counter = Counter(stages)


    for i in range(1,N+1):
        fail_people = counter[i] #실패한 사람 수

        if chamga == 0:
            fail = 0
        else:
            fail = fail_people/chamga

        chamga -= fail_people

        answer.append((i,fail)) # 튜플 자료 구조형으로 스테이지와 실패율을 한번에 저장

    answer = sorted(answer, key=lambda x: x[1], reverse = True) # 저장된 튜플을  sorted 함수와 람다함수를 이용하여 내림차순 정렬

    answer = [i[0] for i in answer] # 정렬된 튜플을 i[0]만 뽑아 리스트를 만든뒤 answer에 저장
    
    return answer



N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]	

print(solution(N,stages))

