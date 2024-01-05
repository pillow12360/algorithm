# 1월 5일 금요일

# dp 포도주 시식 실버1

# bottom - up 방식

n = int(input())

podo = []
dp = [0] * n

for _ in range(n):
    podo.append(int(input()))

if n >= 3:
    dp[0] = podo[0]
    dp[1] = podo[0] + podo[1]  # base case 작성
    for i in range(2, len(podo)):
        a = dp[i-1]
        b = dp[i-2]+podo[i]
        c = dp[i-3]+podo[i-1]+podo[i]
        dp[i] = max(a, b, c)

    print(dp[-1])

elif n == 1:
    print(podo[0])
elif n == 2:
    print(podo[0]+podo[1])
