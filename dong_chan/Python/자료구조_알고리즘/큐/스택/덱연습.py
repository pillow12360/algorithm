from collections import deque


priorities = []

q = deque([(index, value) for index, value in enumerate(priorities)])


'''
초급: 리스트 요소의 제곱 구하기
문제: 주어진 숫자 리스트의 각 요소를 제곱한 새 리스트를 생성하세요.

입력: [1, 2, 3, 4, 5]

예상 출력: [1, 4, 9, 16, 25]
'''
input1 = [1, 2, 3, 4, 5]
answer = [a**2 for a in input1]
print(answer)

'''
중급: 짝수만 필터링하기
문제: 주어진 숫자 리스트에서 짝수만을 추출하여 그 제곱값을 요소로 하는 새 리스트를 생성하세요.

입력: [1, 2, 3, 4, 5, 6]

예상 출력: [4, 16, 36]
'''

input2 = [1, 2, 3, 4, 5, 6]
answer2 = [a ** 2 for a in input2 if a % 2 == 0]
print(answer2)

'''
고급: 문자열 리스트에서 길이가 5 이상인 문자열 찾기
문제: 주어진 문자열 리스트에서 길이가 5 이상인 문자열만을 선택하여, 각 문자열을 대문자로 변환한 새 리스트를 생성하세요.

입력: ["hello", "world", "list", "comprehension", "example"]

예상 출력: ["HELLO", "WORLD", "COMPREHENSION", "EXAMPLE"]
'''

input3 = ["hello", "world", "list", "comprehension", "example"]
answer3 = [i.upper() for i in input3 if len(i) >= 5]
print(answer3)
