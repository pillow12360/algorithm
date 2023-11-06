# 10월 4일 백준 골드 4 

# 수 묶기
'''
n = int(input())

lis = []

for i in range(n):
  lis.append(int(input()))

if n == 1:
  print(lis[0])
else:
  lis.sort(reverse=True)

  answer = []

  for i in range(0,len(lis)-1,2):
    a = lis[i]
    b = lis[i+1]
    if a == 1 and b == 1:
      answer.append(a)
      answer.append(b)
    elif a > 0 and b > 0:
      answer.append(a*b)
    else:
      answer.append(max((a*b),(a+b)))
    if n % 2 != 0:
      answer.append(lis[-1])

  print(sum(answer))

  '''

n = int(input())

plus = []
minus = []

for i in range(n):
  a = int(input())
  if a > 0:
    plus.append(a)
  elif a < 0:
    minus.append(a)
  elif a == 0:
    minus.append(a)

plus.sort()
minus.sort(reverse=True)


answer = []

while plus:
  if len(plus) <= 1:
    a = plus.pop()
    answer.append(a)
  else:
    a = plus.pop()
    b = plus.pop()
    answer.append(max((a*b),a+b))

while minus:
  if len(minus) <= 1:
    a = minus.pop()
    answer.append(a)
  else:
    a = minus.pop()
    b = minus.pop()
    answer.append(a*b)

print(sum(answer))
