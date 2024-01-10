# 1월 10일

# dp 실버 2

n = int(input())

number = list(map(int, input().split()))

dp = [0] * n

dp[0] = number[0]

for i in range(n):
    for j in range(i):
        if number[i] > number[j]:
            dp[i] = max(dp[i], dp[j]+number[i])
        else:
            dp[i] = max(dp[i], number[i])

print(max(dp))

# dp 테이블을 채우기 위해 2중 for문을 돌며 비교하며 진행
# 1차원 dp를 채우면 된다.

#  dp [i] 가 가장 큰 수열의 합으로 풀면 안된다.

# 결과적으로 dp의 값은
# [1,101,3,53,113,6,11,17,24,32]

# dp[i] 는 각 수열의 합이 된다.
# max()를 이용하여 최댓값을 출력
