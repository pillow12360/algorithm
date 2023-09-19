'''
if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

'''
'''
memo = {}

def w(a,b,c): # a,b,c 모두 0보다 작을 때
  if (a,b,c) not in memo:

    if a <= 0 or b <= 0 or c <= 0:
      return 1 
    
    if a > 20 or b > 20 or c > 20:
      return w(20, 20, 20)

    if a < b and b < c: # 오름차순 a,b,c 일때
      return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    
    memo[(a,b,c)] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)

    return memo[(a,b,c)]

while True:
  a, b, c = map(int,input().split())
  if a == -1 and b == -1 and c == -1:
    break
  answer = w(a,b,c)
  print("w(%d, %d, %d) = %d" %(a,b,c,answer))
'''


dp_table = [[[0]*21 for _ in range(21)]for _ in range(21)]

def w(a,b,c): 
  if a <= 0 or b <= 0 or c <= 0:
    return 1 
  
  if a > 20 or b > 20 or c > 20:
    return w(20, 20, 20)

  if dp_table[a][b][c]:
    return dp_table[a][b][c]

  if a < b and b < c:
    dp_table[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
  
  dp_table[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)

  return dp_table[a][b][c]

while True:
  a, b, c = map(int,input().split())
  if a == -1 and b == -1 and c == -1:
    break
  answer = w(a,b,c)
  print("w(%d, %d, %d) = %d" %(a,b,c,answer))

# 이 문제의 핵심은 계산한 값을 저장하는 방법과 재활용 하는 방법을 사용할 줄 아는 것
# 재귀를 이용한 top - down 방식