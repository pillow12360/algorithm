# 8월 9일 오후 11시 49분 약 15분 소요

while True:  
  a , b = map(int,input().split())

  if a == 0 and b == 0:
      break


  ack = []
  bae = []

  if a < b:
      for i in range(1,b+1):
          if b % i == 0:
              ack.append(i)
      if a in ack:
        print("factor")
      else:
          print("neither")
  else:
      if a % b == 0:
        print("multiple")
      else:
          print("neither")

