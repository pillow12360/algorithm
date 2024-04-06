n = int(input())

# n 이하인 제곱 수 중에 가장 큰 수를 구해야 해
answer = 0

while n != 0:
    for i in range(1, n):
        if i**2 <= n and (i+1) ** 2 > n:
            n -= i**2
            answer += 1
            break

print(answer)


number = int(input())

dp = [i for i in range(number + 1)]

for i in range(2, number + 1):
    for j in range(1, i + 1):
        square = j * j
        if square > i:
            break

        if dp[i] > dp[i - square] + 1:
            dp[i] = dp[i - square] + 1

print(dp[number])
