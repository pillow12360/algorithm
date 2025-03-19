from collections import deque

n = int(input())

arr = []

for i in range(n):
  arr.append(list(map(int,input().split())))

answer = deque()

for i in arr:
  if i[0] == 1:
    answer.appendleft(i[1])
  elif i[0] == 2:
    answer.append(i[1])
  elif i[0] == 3:
    print(answer.popleft() if answer else -1)
  elif i[0] == 4:
    print(answer.pop() if answer else -1)
  elif i[0] == 5:
    print(len(answer))
  elif i[0] == 6:
    print(1 if not answer else 0)
  elif i[0] == 7:
    print(answer[0] if answer else -1)
  elif i[0] == 8:
      print(answer[len(answer)-1] if answer else -1)