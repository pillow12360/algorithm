# 파이썬 딕셔너리 메서드 테스트
# 각 문제의 빈칸을 채워보세요

# 기본 문제 (10문제)

# 1. 빈 딕셔너리 `my_dict`를 생성하는 코드를 작성하세요.
my_dict = {}

# 2. 딕셔너리에서 키 'name'의 값을 가져오되, 키가 없을 경우 'Unknown'을 반환하는 코드를 작성하세요.
result = my_dict.get('name', 'Unknown')
print(result)

# 3. 딕셔너리의 모든 키를 가져오는 메서드는 무엇인가요?
all_keys = my_dict.keys()

# 4. 딕셔너리의 모든 값을 가져오는 메서드는 무엇인가요?
all_values = my_dict.values()

# 5. 딕셔너리의 모든 키-값 쌍을 튜플로 가져오는 메서드는 무엇인가요?
all_items = my_dict.items()

# 6. 딕셔너리 `dict1`에 다른 딕셔너리 `dict2`의 모든 키-값 쌍을 추가하는 메서드는 무엇인가요?
dict1 = {
    
}
dict2 = {}

dict1.update(dict2)

# 7. 딕셔너리에서 키 'age'와 그 값을 제거하고, 그 값을 반환하는 코드를 작성하세요.
age = my_dict.pop('age')

# 8. 딕셔너리의 마지막으로 추가된 키-값 쌍을 제거하고 반환하는 메서드는 무엇인가요?
last_item = my_dict.popitem()

# 9. 딕셔너리의 모든 항목을 제거하는 메서드는 무엇인가요?
my_dict.clear()

# 10. 딕셔너리에 키 'score'가 있는지 확인하는 코드를 작성하세요.
has_score = 'score' in my_dict


# 응용 문제 (5문제)

# 11. `names` 리스트의 각 요소를 키로 하고 값은 모두 0으로 설정하는 딕셔너리를 생성하는 코드를 작성하세요.
names = ['Alice', 'Bob', 'Charlie']
scores = dict._____(names, 0)

# 12. 딕셔너리 `user_data`에서 키 'email'이 있으면 그 값을 가져오고, 없으면 키-값 쌍 'email': 'no-email'을 추가하고 'no-email'을 반환하는 코드를 작성하세요.
email = user_data.___('email', 'no-email')

# 13. 1부터 5까지의 수를 키로 하고, 그 제곱을 값으로 하는 딕셔너리를 딕셔너리 컴프리헨션을 사용하여 생성하는 코드를 작성하세요.
squares = {_____}

# 14. Python 3.9 이상에서, 두 딕셔너리 `dict1`과 `dict2`를 합쳐 새 딕셔너리를 만드는 연산자는 무엇인가요?
merged = dict1 _____ dict2

# 15. 딕셔너리 `inventory`의 얕은 복사본을 만드는 메서드는 무엇인가요?
inventory_copy = inventory.clone()


# 실전 문제 (5문제)

# 16. 다음 코드의 출력 결과는 무엇인가요?
data = {'a': 1, 'b': 2}
data.update({'b': 3, 'c': 4})
print(data)
# 출력 결과: {'a' : 1, 'b' : 3, 'c': 4}

# 17. 다음 코드의 출력 결과는 무엇인가요?
data = {'a': 1, 'b': 2, 'c': 3}
item = data.popitem()
print(item)
print(data)
# 출력 결과 1: {'c' : 3}
# 출력 결과 2: {'a' : 1, 'b' : 2}

# 18. 다음 코드의 출력 결과는 무엇인가요?
data = {'a': 1, 'b': 2}
value = data.setdefault('c', 3)
print(value)
print(data)
# 출력 결과 1: {'a' : 1, 'b' : 2, 'c' : 3}
# 출력 결과 2: {'a' : 1, 'b' : 2, 'c' : 3}

# 19. 다음 코드의 출력 결과는 무엇인가요?
keys = ['a', 'b', 'c']
values = [1, 2, 3]
data = dict(zip(keys, values))
print(data)
# 출력 결과: {'a' : 1, 'b' : 2, 'c' : 3}

# 20. 다음 코드의 출력 결과는 무엇인가요?
data = {'a': 1, 'b': 2}
try:
    print(data['c'])
except KeyError:
    print(data.get('c', 'Not found'))
# 출력 결과: 'Not found'

"""
# 정답

# 기본 문제:
# 1. {}
# 2. get
# 3. keys
# 4. values
# 5. items
# 6. update
# 7. pop
# 8. popitem
# 9. clear
# 10. 'score'

# 응용 문제:
# 11. fromkeys
# 12. setdefault
# 13. x: x**2 for x in range(1, 6)
# 14. |
# 15. copy

# 실전 문제:
# 16. {'a': 1, 'b': 3, 'c': 4}
# 17. ('c', 3) 및 {'a': 1, 'b': 2}
# 18. 3 및 {'a': 1, 'b': 2, 'c': 3}
# 19. {'a': 1, 'b': 2, 'c': 3}
# 20. 'Not found'
"""
