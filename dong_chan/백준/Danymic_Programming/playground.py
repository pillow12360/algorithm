def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        dp = [0] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + i
        return dp[n]
    
# print(sum_of_digits(10))

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# def fibonacci(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         dp = [0] * (n + 1)
#         dp[0] = 0
#         dp[1] = 1
#         for i in range(2, n + 1):
#             dp[i] = dp[i - 1] + dp[i - 2]
#         return dp[n]

print(fibonacci(10))