number = list(input().split())
hap = 0
for i in number:
  hap += int(i)**2
print(hap%10)