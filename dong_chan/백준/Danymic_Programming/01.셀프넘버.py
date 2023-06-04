# 동적프로그래밍 6월2일

# 답지 확인 함

# 집합 자료형은 요소값의 중복을 허용하지 않음

set1 = set(range(1,10001)) #1부터 10000까지의 모든 요소 리스트를 집합자료형으로 저장 
# -연산자로 차집합을 구하기 위함

remove_set = set() #이것 역시 집합 자료형

for i in set1:
    for num in str(i): #스트링형으로 변환후 모든 익덱스 반복
        i += int(num)
    remove_set.add(i)

self_numbers = set1 - remove_set # 차집합을 구함

for i in sorted(self_numbers):
    print(i)