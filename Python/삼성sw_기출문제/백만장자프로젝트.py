n = int(input())

price = list(map(int,input().split()))

max_price = 0 # 가장 큰 판매 금액
max_profit = 0 # 수익

for i in range(n-1,-1,-1):
  if price[i] > max_price:
    max_price = price[i]
  else:
    max_profit += max_price - price[i]

print(max_profit)