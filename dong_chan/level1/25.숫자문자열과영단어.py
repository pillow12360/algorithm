def solution(s):
    answer = 0
    
    numbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]

    for i in numbers:
        if i in s:
            s = s.replace(i,str(numbers.index(i)))
    answer = int(s)


    return answer

s="123"
print(solution(s))

# replace 함수와 index 함수 사용
# python의 in 의 활용법