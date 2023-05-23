def solution(strings, n):
    answer = []

    alpha = []

    for i in strings:
        alpha.append(i[n])
    # 정렬 기준 알파벳 구하기

    dic1 = {}

    for i, j in enumerate(alpha):
        dic1[i]=j
    # 딕셔너리로 인덱스와 값을 한번에 저장
    # 오류 발생 키값이 같으면 값이 삭제됨 values 값을 알파벳 원소로


    dic1 = dict(sorted(dic1.items()))

    # values 를 오름차순 정렬 
    #리스트 변환 문제 해결 but 집합 자료형으로 변환 => dict() 함수로 해결

    print(dic1)

    for i in dic1.keys():
        
        if dic1[i] == dic1[i+1]:
            temps = []
            temps.append(strings[i])
            temps.append(strings[i+1])
            temps = sorted(temps)
            for j in temps:
              answer.append(j)
            i+=1
        else:
          answer.append(strings[i])
    

    return answer

# N 인덱스 값의 알파벳으로 오름차순 정렬 하는 코드

# 파이썬의 딕셔너리 자료형으로 원래의 인덱스 값과 데이터를 가지고 정렬한뒤
# 정렬한 값 대로 원래의 인덱스로 strings의 순서를 바꾸는 방법
strings = ["abce", "abcd", "cdx"]	
n = 2

print(solution(strings,n))
