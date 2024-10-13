# 1월 12일 dp
# 이항 계수 2
# 실2

N, K = map(int, input().split())

dp = []

for i in range(N+1):
    dp.append([1]*(i+1))

for i in range(2, N+1):
    for j in range(1, i):
        dp[i][j] = (dp[i-1][j-1]+dp[i-1][j]) % 10007

print(dp[N][K])

# 조합론의 개념
# 이항 계수
'''
n과 k에 대해, 
n개의 서로 다른 원소에서 
k개를 순서에 상관없이 선택하는 방법의 수
'''
