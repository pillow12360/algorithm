def solution(s, n):
    answer = ''
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s=" ".join(s.split(" "))
    # 공백 중복 제거

    for i in s:
        if i.islower(): #소문자일때
          sIndex = lower.find(i)
          returnIndex = sIndex+n
          if returnIndex >= 26:
              returnIndex -= 26
          answer += str(lower[returnIndex])
        elif i.isupper(): #대문자 일때
            sIndex = upper.find(i)
            returnIndex = sIndex+n
            if returnIndex >= 26:
              returnIndex -= 26
            answer += str(upper[returnIndex])
        elif i == " ":
           answer += " "

    return answer

s = "a B z"
n = 4
print(solution(s,n))



lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 알스웨트가이 파이썬 프로젝트 #6 카이사르 암호와 같은 내용

#ord(문자) 아스키로 반환
#chr(숫자) 해당 문자로 반환

#소문자 및 대문자 문자열이 넘어갈 경우 다시 처음부터 시작할 대응 마련해야함


# 1방법 : 문자열 대응 방법
# string.find(), string.index()
plus = 1
s1= "z"
sIndex = lower.find(s1)

# print(lower[lower.find("z")+plus]) #오류 발생 인덱스 값 범위 벗어남

returnIndex = sIndex+plus

if returnIndex >= 26:
    returnIndex -= 26
# 인덱스 범위가 벗어날 경우 해결 방안

print(lower[returnIndex])

# 2방법 아스키 코드 변환 방법
