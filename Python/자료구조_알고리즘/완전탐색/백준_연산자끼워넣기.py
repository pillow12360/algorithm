# 11월 7일 화요일

# 삼성 sw 기출문제 브루트 포스 연산자 끼워 

from itertools import permutations
from collections import deque

N = int(input()) 

nums = list(map(int, input().split())) # 계산할 수의 리스트

cal_input = list(map(int, input().split())) # 각 연산자의 개수 리스트

cal = ["+","-","*","//"]

cal_list = [] # 연산자의 갯수만큼 저장 할 연산자 리스트 (순열을 구하기 위함)

for i in range(4):
  if cal_input[i] == 0:
    pass
  else:
    for j in range(cal_input[i]):
      cal_list.append(cal[i])

num_case = list(permutations(cal_list, len(cal_list)))

queue = deque(num_case)

max_result = -1e9
min_result = 1e9

while queue:
  current_list = queue.popleft()
  result = nums[0]

  for i in range(1, len(nums)):
    if current_list[i-1] == '+':
      result += nums[i]
    elif current_list[i-1] == '-':
      result -= nums[i]
    elif current_list[i-1] == "*":
      result *= nums[i]
    else:
      if result < 0:
        result = -(abs(result)//nums[i])
      else:
        result = result // nums[i]

  max_result = max(result, max_result)
  min_result = min(result, min_result)

print(max_result)
print(min_result)