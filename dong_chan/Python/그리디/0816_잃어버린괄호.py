# 08월 16일 수요일
# 정답 확인 함 (실패)


# 이 문제의 핵심은 가장 작은 수 를 출력 하는 것
# -를 기준으로 문자열을 끊어 준다.
# list.split('-') 은 -를 기준으로 문자열을 여러개로 나누어줌

a = str(input())

b = a.split('-')
print(b)

answer = 0


x = sum(map(int, (b[0].split('+'))))

if a[0] == '-':
    answer -= x
else:
    answer += x

for i in b[1:]:
    x = sum(map(int, (i.split('+'))))
    answer -= x

print(answer)
