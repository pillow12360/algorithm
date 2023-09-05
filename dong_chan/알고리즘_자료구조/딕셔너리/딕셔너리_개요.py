# 08월 19일 토요일 공부 2 딕셔너리 자료구조

# score = [97,49,89]

# 수학 국어 영어
# 무엇이 수학 국어 영어 점수인가 ?

# 딕셔너리 선언

score = {
    'math': 97,
    'eng': 49,
    'kor': 89
}

# 각 과목은 key 이고 과목당 점수는 value
# 는 유일해야한다.

score['math'] = 45
# 접근 및 수정

score['sci'] = 100
# 추가

print(score['math'])
print(score['sci'])

# 특정 key의 유무를 확인한다. 'in연산자'

# in은 O(1) 으로 특정 키의 유무를 확인할 수 있다. = 이것은 매우 유용함

print('music' in score)

if 'music' in score:
    print(score['music'])
else:
    score['music'] = 0
    print(score['music'])

# 딕셔너리는! 시간복잡도를 줄이기 위해 메모리를 사용하는 것이다!

# 내부동작이 어떻게 동작하는지 이해해야함
# in 연산자는 랜덤엑세스로 동작한다.
