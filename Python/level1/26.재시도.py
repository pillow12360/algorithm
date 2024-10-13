def solution(strings,n):
    answer = []
    list1 = []

    for i in strings:
        list1.append((i,i[n]))
    
    list1 = sorted(list1,key=lambda x : (x[1],x[0]))
    #sorted의 키값을 x[1]을 지정하면 1번째 인덱스를 기준으로 오름차순 정렬해준다. 만약 x[1] 값이 중복되었을 때는 (x[1],x[0])처럼 x[0] 또한 오름차순으로 정렬해준다. 
    answer = [i[0] for i in list1]

    return answer

#sorted_name = [x for _, x in sorted(zip(list1, name), key=lambda pair: (pair[0], pair[1]))]

strings = ["sun", "bed", "car"]	
n = 1

print(solution(strings,n))