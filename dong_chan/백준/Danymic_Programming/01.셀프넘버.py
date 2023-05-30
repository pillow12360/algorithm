set1 = set(range(1,10001))

remove_set = set()
for i in set1:
    for num in str(i): #str의 인덱스값을 반복
        i += int(num)
    remove_set.add(i) # set의 추가하는 함수 add , 리스트는 append

self_numbers = set1 - remove_set # set자료형 차집합을 구하는 방법

for i in sorted(self_numbers): # set은 정렬되어 있지 않으므로 sorted사용
    print(i)