str = input()
answer = []
for i in str:
  if i.islower():
    answer.append(i.upper())
  else:
    answer.append(i.lower())
for i in answer:
  print(i, end="")