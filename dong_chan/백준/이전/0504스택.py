
def stackfunc(A,B):
    if A == "push":
      stack.append(B)

    elif A == "pop":
      if not stack:
        print("-1")
      else:
        P = stack.pop()
        print(P)
      
    elif A == "size":
      print(len(stack))

    elif A == "empty":
      if stack:
        print("0")
      else:
        print("1")

    elif A == "top":
      if stack:
        print(stack[-1])
      else:
        print("-1")


num = int(input())

stack = []

while(num>0):

  C = input()
  if " " in C:
    A, B = C.split()
    A = str(A)

  else:
    A = str(C)
    B = 0

  stackfunc(A,B)

  num += -1

