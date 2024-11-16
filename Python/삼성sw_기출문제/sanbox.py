

nums =[1,2,3,4,5]

nums = set(nums)

# [표현식 for 변수 in 반복가능한_객체 if 조건]

num1 = [ x ** 2 for x in nums if x % 2 == 0]

print(num1)

print(list(range(1,10)))

a = list(range(1,10))

print(a)

dic = {1: "bye", 2: "hello"}

value = dic[1]
value2 = dic[2]

print(value, value2)

print(dic.pop(1))

print(dic)

dict1 = {'a': 1, 'b': 2, 'c': 3}

# 키 목록
keys = dict1.keys()      # dict_keys(['a', 'b', 'c'])

print(keys)

# 값 목록
values = dict1.values()  # dict_values([1, 2, 3])

print(values)
# 키-값 쌍 목록
items = dict1.items()    # dict_items([('a', 1), ('b', 2), ('c', 3)])

print(items)

def is_valid(x,y,n,m):
    return 0 <= x < n and 0 <= y < m