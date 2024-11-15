'''
def backtrack(m, n):
  if 

  for i in range()


'''
'''
n, s = map(int, input().split())

num = list(map(int,input().split(" ")))

print(num)

dap = 0

def backtrack(candi, num):
  global dap

  if candi and sum(candi) == s:
    dap += 1
    return
  # elif sum(candi) > s:
  #   return
  
  else:
      for i in num:
        candi.append(i)
        backtrack(candi, num)
        candi.pop()

candi = []

backtrack(candi ,num)

print(dap)
'''
n, s = map(int, input().split())
num = list(map(int, input().split()))

dap = 0

def backtrack(idx, total):
    global dap
    
    if idx >= n:
        return
        
    total += num[idx]
    
    if total == s:
        dap += 1
        
    backtrack(idx + 1, total)  # 현재 수를 선택한 경우
    backtrack(idx + 1, total - num[idx])  # 현재 수를 선택하지 않은 경우
    
backtrack(0, 0)
print(dap)