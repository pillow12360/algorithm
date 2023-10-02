#9월 25일 월요일

# 백준 실버1 쉬운 계단 수
# 정답 확인


n = int(input())


dp=[[0]*10 for _ in range(n+1)]
# dp 테이블은 올 수 있는 경우의 수를 저장 하여 모두 더하는 형식

for i in range(1,10):
  dp[1][i] = 1
# 베이스 케이스 지정

for i in range(2,n+1):
  for j in range(10):
    if j == 0:
      dp[i][j] = dp[i-1][1]
    elif j == 9:
      dp[i][j] = dp[i-1][8]
      # 9는 8만 붙을 수 있음
    else:
      dp[i][j] = dp[i-1][j+1] + dp[i-1][j-1]

# j 가 0일 경우
# j 가 9일 경우
# j 가 1~8 까지일 경우

count = sum(dp[n])

print(count % 1000000000)