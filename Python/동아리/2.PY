car1 = input()
car2 = input()

X = len(car1) + 1
Y = len(car2) + 1

dp = [[0]*Y for _ in range(X)]

length = 0

for i in range(1,Y):
  for j in range(1,X):
    if car1[i] == car2[j]:
      dp[i][j] = dp[i-1][j-1] + 1
      length = max(dp[i][j],length)
    else:
      dp[i][j] = 0

print(dp)
print(length)