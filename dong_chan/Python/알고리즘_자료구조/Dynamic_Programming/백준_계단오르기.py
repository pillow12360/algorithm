# 9월 20일 수요일 dp 계단 오르기 실버3 

# 점수의 최댓값을 구해야 함

# top - down 방식으로 


# 1. 한칸 또는 두칸 씩 
# 2. 연속된 3칸을 이동해서는 안된다.
# 3. 마지막 계단은 무조건 밟아야 함

# score = [0,10,20,15,25,10,20]

# len_stair = len(score)

# sum = [0 for _ in range(len_stair)]

# def sum_score(N):
#   if N == 0:
#     sum[N] = score[0]
#     return sum
#   if N == 1:
#     sum[N] = score[1]
#     return sum
#   if N == 2:
#     sum[N] = score[1] + score[2]
#     return 
#   if N > 2:
#     sum[N] = score[N] + max(score[N-2],score[N-1])

# n = len_stair-1

# def max_score ():
#   max_value = 0
#   if n == 0:
#     return 0
#   if n == 1:
#     return score[1]
#   if n == 2:
#     return score[1]+score[2]
#   if n > 3:
#     return score[n] + max(score[n-2],score[n-1])

#   a =max_score(n-2)
#   b =max_score(n-1)

#   max_value = max(a,b)+score[n-1]

#   return max_value

# print(max_score(n))

# bottom - up 방식 

n = int(input())

stair = [int(input()) for _ in range(n)]

dp_table = [0] * n

if len(stair) < 3:
  print(sum(stair))
else:
  dp_table[0] = stair[0]
  dp_table[1] = stair[0] + stair[1]
  for i in range(2,n):
    dp_table[i] = max(dp_table[i-3]+stair[i-1]+stair[i], dp_table[i-2]+stair[i])
  print(dp_table[-1])

