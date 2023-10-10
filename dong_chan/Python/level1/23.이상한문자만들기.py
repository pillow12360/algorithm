# 대문자, 소문자로 바꾸는 메서드 upper() , lower()

#capitalize() : 맨 첫글자만 대문자로 변환

# 파이썬의 공백나누기 메서드 문자열.split("나눌기준문자") , 와 문자열.join('합칠문자')

# 위 두 함수는 리턴값이 리스트 형식으로 반환 요소는 문자열

# for i in s:
#         for j in range(len(i)): #s 리스트의 요소 i의 반복문을 돌려 j(각 단어에 대한 반복문 짝수이면 대문자 출력 아니면 그냥 출력 print() 함수의 end 인자를 변경하여 출력
#             if j % 2 == 0:
#                 print(i[j].upper(),end="")
#             else:
#                 print(i[j],end="")
#         print(" ",end="")

def solution(s):
    answer = ''
    s = ' '.join(s.split())
    s = s.split(' ') # s를 공백기준으로 나누어 리스트와 시킨다.
    for i in s:
      for j in range(len(i)): 
        if j % 2 == 0:
          answer+=i[j].upper()
        else:
          answer+=i[j].lower()
      answer+=" "
    answer = answer.strip() # 마지막 공백 제거

    return answer

s = "abc    abcd   abcde   frd"

print(solution(s))

