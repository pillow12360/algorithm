# 최장 공통 부분 수열(LCS) 10월6일 복습

string1 = input()
string2 = input()

X = len(string1) + 1
Y = len(string2) + 1

dp = [[0] * Y for _ in range(X)] # dp 테이블 초기화

for y in range(1, Y):
    for x in range(1, X):
        if string1[y-1] == string2[x-1]:
            dp[y][x] = dp[y-1][x-1] + 1
        else:
            dp[y][x] = max(dp[y][x-1], dp[y-1][x])

print(dp[-1][-1])