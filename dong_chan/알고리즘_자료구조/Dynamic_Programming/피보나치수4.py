# 실버 5 dp 피보나치 수

n = int(input())

dp = [0] 
def fibo(n):
  if dp[n]:
    return 1
  return fibo(n-2) + fibo(n-1)

print(fibo(n))