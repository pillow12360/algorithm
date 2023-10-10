import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def size(self):
        return len(self.stack)

    def empty(self):
        if self.stack:
            return 0
        else:
            return 1

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1


def stackfunc(A, B, stack):
    if A == "push":
        stack.push(B)
    elif A == "pop":
        return stack.pop()
    elif A == "size":
        return stack.size()
    elif A == "empty":
        return stack.empty()
    elif A == "top":
        return stack.top()


num = int(sys.stdin.readline())
stack = Stack()

result = []

while num > 0:
    C = sys.stdin.readline().rstrip()
    if " " in C:
        A, B = C.split()
    else:
        A = C
        B = None
    res = stackfunc(A, B, stack)
    if res is not None:
        result.append(str(res))
    num -= 1

sys.stdout.write("\n".join(result))