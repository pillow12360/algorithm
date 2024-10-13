'''
(심심할떄 풀어보기 2.)
-부품 정비를 위해 2대의 차의 정비기록을 비교하여 정비를 시작한다. 두 대의 자동차는 각각 문자열로 주어지며, 두 대의 자동차 문자열이 최대로 공통된 부분을 출력해야 한다.
단, 두 대의 자동차 문자열 중 최대 1회만큼 중간에 문자열을 바꿀 수 있다.
(자동차 1에서 문자열 하나 바꾸었으면, 자동차 2에서는 문자열을 바꿀 수 없음)
(자동차 2에서 문자열 하나 바꾸었으면, 자동차 1에서는 문자열을 바꿀 수 없음)

예)

테스트 케이스

입력

ABCDG
AEDG

출력

ACDG

'''
'''
car1 = input().strip()
car2 = input().strip() # 문자열 입력

X = len(car1)
Y = len(car2)

car_max_len = max(X,Y)

if X != car_max_len: # 두 문자열의 길이가 다른 경우 _ 값으로 문자열의 길이를 서로 맞추어줌
  plus = '_' * (car_max_len - X) 
  car1 = plus + car1
if Y != car_max_len:
  plus = '_'*(car_max_len - Y)
  car2 = plus + car2

print(car1)
print(car2)

X = car_max_len + 1 # dp 테이블의 0 값 추가 하기 위해 1 추가
Y = car_max_len + 1 

# bottom-up

dp_table = [[0]*(Y) for _ in range(X)]

answer = ""

for y in range(1,Y):
  for x in range(1,X):
    if car1[y-1] == car2[x-1]:
      dp_table[y][x] = dp_table[y-1][x-1] + 1
      answer += car1[y-1]
    else:
      dp_table[y][x] = 0

print(dp_table)
print(answer)

# 수열일 경우 한번 
'''

'''

car1 = input()
car2 = input()

X = len(car1)
Y = len(car2)

car_max_len = max(X,Y)

if X != car_max_len:
  plus = '_' * (car_max_len - X) 
  car1 = plus + car1
if Y != car_max_len:
  plus = '_'*(car_max_len - Y)
  car2 = plus + car2

X = car_max_len
Y = car_max_len


dp = [[0 for _ in range(Y+1) for _ in range(X+1)]]

# dp 테이블 초기화

longest_length = 0

for i in range(1, Y+1):
  for j in range(1, X+1):
    if car1[i] == car2[j]:
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = 0 
    longest_length = max(longest_length, dp[i][j])

print(longest_length)

'''

def find_max_common_substring(car1, car2):
    m, n = len(car1), len(car2)
    
    # Initialize a 2D DP table to store the length of common substrings.
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize a flag to track if a single edit has been used.
    edit_used = False
    
    max_length = 0
    max_i = 0
    max_j = 0
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if car1[i - 1] == car2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
            if dp[i][j] > max_length:
                max_length = dp[i][j]
                max_i = i
                max_j = j
    
    # Construct the common substring.
    common_substring = []
    while max_i > 0 and max_j > 0:
        if car1[max_i - 1] == car2[max_j - 1]:
            common_substring.append(car1[max_i - 1])
            max_i -= 1
            max_j -= 1
        else:
            if not edit_used:
                edit_used = True
            else:
                break
            max_i -= 1
            max_j -= 1

    common_substring.reverse()
    
    return "".join(common_substring)

# Example usage:
car1 = "ABCDG"
car2 = "AEDG"

result = find_max_common_substring(car1, car2)
print("Maximum Common Substring with 1 Edit Allowed:", result)