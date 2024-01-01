#1월1일 그리디 골드 5
# A와 B




S = list(input())
T = list(input())

# print(S,T)

# Top - down 방식 풀이
dap = False

while T:

  if T[-1] == 'A':
    T.pop()

  elif T[-1] == 'B':
    T.pop()
    T.reverse()

  if S == T:
    dap = True
    break
  

if dap:
  print(1)
else:
  print(0)

