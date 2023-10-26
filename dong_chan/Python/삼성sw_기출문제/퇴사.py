# 10월 18일 퇴사 (실버2)
# 알고리즘 분류 보지 않고 진행

# 삼성 sw 기출 문제 1일차

'''
for i in range(N): # 일정보다 넘어가는 상담 미리 제거
  if date[i][0] > N - i:
    reserved[i] = True


for i in range(N-1):
  if date[i][0] == 1 and not reserved[i]:
    reserved[i] = True
    dap += date[i][1]
  else: 
    if reserved[i+1] == True and date[i][0] < N - (i-1):
      for i in range(date[i][0]):
          reserved[i] = True
      dap += date[i][1]
      if (date[i][1]/date[i][0] >= date[i+1][1]/date[i+1][0]) and not reserved:
        for i in range(date[i][0]):
          reserved[i] = True
        dap += date[i][1]

if (reserved[N-1] == False):
  dap += date[N-1][1]
  reserved[N-1] = True
'''

N = int(input())

date = []

for _ in range(N):
  T , P = map(int,input().split())
  date.append((T,P))

dp = [0] * (N+1) 
# dp[i] 의 값은 이 날짜까지의 최대로 상담을 한 이익

for i in range(N):
  for j in range(i+date[i][0], N+1):
    if dp[j] < dp[i] + date[i][1]:
      dp[j] = dp[i] + date[i][1]

print(dp[-1])