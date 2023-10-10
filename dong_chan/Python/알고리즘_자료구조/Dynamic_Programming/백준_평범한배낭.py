# 10월2일 평범한 배낭 dp 골드5
# from itertools import combinations

'''
n, k = map(int,input().split())

item = []

for _ in range(n):
  item.append(tuple(map(int,input().split())))

print(item)

comb = []
comb = [combinations(item,2)]

for i in range(1,n+1):
  for j in combinations(item,i):
    if  
'''

'''
최대 한도의 용량이 설정되어 있을 때 최대한의 가치를 가지도록 배낭을 싸야함 


knapsak 알고리즘 

n * k 의 2차원 리스트를 활용하여 n까지 살펴보았을 때 무게가 k인 배낭의 최대 가치


'''

n , k = map(int,input().split())

dp = [[0] * (k+1) for _ in range(n+1)]

item = [[0,0]] # 인덱스를 헷갈리지 않게 요소 하나 추가 X (i - 1 인덱스의 예외 처리)

for i in range(n):
  item.append(list(map(int,input().split())))

# 담을 물건의 인덱스 : i , 무게 : w , 가치 : v
# 넣을 수 있는 무게 : j

for i in range(n+1):
  for j in range(k+1):
    w = item[i][0]
    v = item[i][1]

    if j < w: # 담을 무게가 넣을 수 있는 무게를 초과 하면 넣지 않는다.
      dp[i][j] = dp[i-1][j] # 넣지 않으므로 전의 값을 대입
    else: # 넣는다면,
      dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)
      # 넣지않는 것과, 넣는 것을 비교하여 더 큰 값을 대입

# print(dp)
print(dp[n][k])
