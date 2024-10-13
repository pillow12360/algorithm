'''
기본 단계: 단순 리스트 정렬
정수 리스트 정렬: 정수로 이루어진 리스트를 오름차순으로 정렬하세요.

기본 단계
정수 리스트 정렬:
입력: [34, 67, 23, 1, 89, 2, 33]
문자열 길이로 정렬:
입력: ["banana", "apple", "cherry", "blueberry"]

문자열 길이로 정렬: 문자열로 이루어진 리스트를 각 문자열의 길이에 따라 오름차순으로 정렬하세요.

중급 단계: 튜플이나 객체의 특정 필드로 정렬
튜플의 두 번째 요소로 정렬: (이름, 점수) 형태의 튜플로 이루어진 리스트를 점수(두 번째 요소)에 따라 오름차순으로 정렬하세요.

딕셔너리 값을 기준으로 정렬: {'이름': 점수} 형태의 딕셔너리를 점수에 따라 오름차순으로 정렬된 키의 리스트를 반환하세요.

고급 단계: 복합 조건으로 정렬
다중 조건으로 문자열 정렬: 문자열로 이루어진 리스트를 먼저 문자열의 길이에 따라 오름차순으로 정렬하고, 길이가 같은 경우 사전 순으로 정렬하세요.

튜플 리스트의 다중 조건 정렬: (이름, 나이, 점수) 형태의 튜플로 이루어진 리스트를 먼저 나이에 따라 오름차순으로 정렬하고, 나이가 같은 경우 점수에 따라 내림차순으로 정렬하세요.
'''


input = [34, 67, 23, 1, 89, 2, 33]


answer1 = sorted(input)


print(answer1)


input2 = ["banana", "apple", "cherry", "blueberry"]
answer2 = sorted(input2, key=lambda x: len(x))
print(answer2)


input3 = [("Tom", 55), ("Jane", 12), ("Max", 25), ("Alice", 32)]
answer3 = sorted(input3, key=lambda x: x[1])
print(answer3)

input4 = {"Tom": 55, "Jane": 12, "Max": 25, "Alice": 32}
answer4 = sorted(input4, key=lambda x: input4[x])
print(answer4)


input5 = ["banana", "pear", "apple", "cherry", "blueberry", "kiwi"]
answer5 = sorted(input5, key=lambda x: (len(x), x))
print(answer5)

input6 = [("Tom", 30, 88), ("Jane", 25, 92), ("Max", 20, 68),
          ("Alice", 25, 100), ("Bob", 30, 95)]
answer6 = sorted(input6, key=lambda x: (x[1], x[2]))
print(answer6)
