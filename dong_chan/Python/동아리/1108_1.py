'''
(심심할떄 풀어보기 1.)
-배터리 용량 관리하기 위해 두 개의 그룹에서 불량여부를 확인하고 있다. 두 개의 그룹 V1, V2를 입력받아 V1, V2 에서 각각 하나의 숫자를 골라 이진 수로 변환 시 가장 1의 개수가 많은 경우를 출력하시오.

 예)
5 4 // 5 : V1 그룹 데이터 개수, 4 : V2 그룹 데이터 개수
2 3 5 7 8
1 4 6 8
'''

# 이진 변환 bin()

'''
import math
import time
import datetime

start = time.time()

V1, V2 = map(int, input().split()) 

v1_list = list(map(int,input().split()))
v2_list = list(map(int,input().split()))

v1_binNum = [] #이진값의 1 개수를 저장할 리스트
v2_binNum = []

for i in v1_list: # v1의 모든 요소를 순회 하며
  cnt = 0 # 각 요소당 1의 개수를 저장 할 변수
  a = str(bin(i)) # 1의 개수를 세기 위해 str 값으로 변환
  for j in a: # str을 순회하며 1갯수 세기
    if j == "1":
      cnt += 1
  v1_binNum.append(cnt)
  print(f'{i}의 이진값의 1개수는 : {cnt}')

v1_max = max(v1_binNum) #가장 많은 경우의 수

print(f'V1의 1이 가장 많은 경우의 수는 {v1_max}')

for i in v2_list:
  cnt = 0
  a = str(bin(i))
  for j in a:
    if j == "1":
      cnt += 1
  v2_binNum.append(cnt)
  print(f'{i}의 이진값의 1개수는 : {cnt}')

v2_max = max(v2_binNum)

print(f'V2의 이진값 중 1이 가장 많은 경우의 수는 {v2_max}')

print(f'V1과 V2 리스트 중 1이 가장 많은 경우는 : {max(v1_max,v2_max)} 입니다.')


end = time.time()

sec = (end - start)
result = datetime.timedelta(seconds=sec)
print(result)

result_list = str(datetime.timedelta(seconds=sec)).split(".")
print(result_list[0])

# 출처: https://blockdmask.tistory.com/549 [개발자 지망생:티스토리]
'''

'''
import math
import time


V1, V2 = map(int, input().split())

# 이진 변환 bin()

v1_list = list(map(int,input().split()))
v2_list = list(map(int,input().split()))

start = time.time()

v1_binNum = []
v2_binNum = []
for i in v1_list:
  cnt = str(bin(i)).count("1")
  v1_binNum.append(cnt)
  print(f'{i}의 이진값의 1개수는 : {cnt}')

v1_max = max(v1_binNum)

print(f'V1의 1이 가장 많은 경우의 수는 {v1_max}')

for i in v2_list:
  cnt = str(bin(i)).count("1")
  v2_binNum.append(cnt)
  print(f'{i}의 이진값의 1개수는 : {cnt}')

v2_max = max(v2_binNum)

print(f'V2의 이진값 중 1이 가장 많은 경우의 수는 {v2_max}')

print(f'V1과 V2 리스트 중 1이 가장 많은 경우는 : {max(v1_max,v2_max)} 입니다.')
end = time.time()

print(f"{end - start:.5f} sec")
# 출처: https://blockdmask.tistory.com/549 [개발자 지망생:티스토리]

'''



import math
import time


V1, V2 = map(int, input().split()) 

v1_list = list(map(int,input().split()))
v2_list = list(map(int,input().split()))

start = time.time()

v1_binNum = [] #이진값의 1 개수를 저장할 리스트
v2_binNum = []

for i in v1_list: # v1의 모든 요소를 순회 하며
  cnt = 0 # 각 요소당 1의 개수를 저장 할 변수
  a = str(bin(i)) # 1의 개수를 세기 위해 str 값으로 변환
  for j in a: # str을 순회하며 1갯수 세기
    if j == "1":
      cnt += 1
  v1_binNum.append(cnt)
  print(f'{i}의 이진값의 1개수는 : {cnt}')

v1_max = max(v1_binNum) #가장 많은 경우의 수

print(f'V1의 1이 가장 많은 경우의 수는 {v1_max}')

for i in v2_list:
  cnt = 0
  a = str(bin(i))
  for j in a:
    if j == "1":
      cnt += 1
  v2_binNum.append(cnt)
  print(f'{i}의 이진값의 1개수는 : {cnt}')

v2_max = max(v2_binNum)

print(f'V2의 이진값 중 1이 가장 많은 경우의 수는 {v2_max}')

print(f'V1과 V2 리스트 중 1이 가장 많은 경우는 : {max(v1_max,v2_max)} 입니다.')

end = time.time()

print(f"{end - start:.5f} sec")
# 출처: https://blockdmask.tistory.com/549 [개발자 지망생:티스토리]