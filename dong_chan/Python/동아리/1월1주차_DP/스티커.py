# 1월 5일 카드

# dp 실버 1

T = int(input())

while T > 0:
    n = int(input())

    card = [[0] * n for _ in range(2)]

    for i in range(2):
        card[i] = (list(map(int, input().split())))

    dp = [[0] * n for _ in range(2)]

    dp[0][0] = card[0][0]
    dp[1][0] = card[1][0]

    if n == 1:
        print(max(dp[0][n-1], dp[1][n-1]))
        T -= 1
        continue

    dp[0][1] = dp[1][0] + card[0][1]
    dp[1][1] = dp[0][0] + card[1][1]

    if n > 2:
        for i in range(2, n):
            dp[0][i] = max(dp[1][i-1]+card[0][i], dp[1][i-2] +
                           card[0][i])
            dp[1][i] = max(dp[0][i-1]+card[1][i], dp[0][i-2] +
                           card[1][i])

    print(max(dp[0][n-1], dp[1][n-1]))

    T -= 1
