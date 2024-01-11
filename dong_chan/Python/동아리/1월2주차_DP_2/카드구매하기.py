# 1월 11일
# 카드 구매하기 dp 실버1

n = int(input())

cost = [0] + list(map(int, input().split()))

dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + cost[j])

print(dp[-1])

'''
dp[i] = 카드 i개를 구매할 때 최대 비용

dp[1] = p[1] -> 한개 구매할 때 최대 비용

dp[2] = dp[1] + cost[1] or dp[0] + cost[2] # 1개 팩 2개냐 , 2개 팩 1개 비교

dp[3] = dp[2] + cost[1] or dp[1] + cost[2] or dp[0] + cost[3]

dp[4] = dp[3] + cost[1] or dp[2] + cost[2] or dp[1] + cost[3] or dp[0] + cost[4]

모든 경우의 수를 찾는 것
'''
