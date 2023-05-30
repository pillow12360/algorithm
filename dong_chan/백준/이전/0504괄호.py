def PS(A):
    stack = []
    for i in A:
        if i == "(":
            stack.append(")")
        elif not stack or stack.pop() != i:
            return "NO"
    if stack  :
        return "NO"
    else:
        return "YES"

num = int(input())

while (num>0):
    A = input()
    print(PS(A))
    num -= 1

