import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def size(self):
        current = self.head
        num = 0
        while current:
            current = current.next
            num += 1
        return num

    def empty(self):
        if self.head is None:
            return 1
        else:
            return 0

    def pop(self):
        if self.head is not None:
            current = self.head
            value = current.value
            self.head = current.next
            return value
        else:
            return -1

    def front(self):
        if self.head is not None:
            return self.head.value
        else:
            return -1

    def back(self):
        if self.head is not None:
            current = self.head
            while current.next:
                current = current.next
            return current.value
        else:
            return -1

def stackfunc(A, B, stack):
    if A == "push":
        stack.push(B)
    elif A == "pop":
        return stack.pop()
    elif A == "empty":
        return stack.empty()
    elif A == "front":
        return stack.front()
    elif A == "size":
        return stack.size()
    elif A == "back":
        return stack.back()

num = int(input())

ll = LinkedList()

results = []

for _ in range(num):
    C = sys.stdin.readline().rstrip()
    if " " in C:
        A, B = C.split()
    else:
        A = C
        B = None
    result = stackfunc(A, B, ll)
    if result is not None:
        results.append(str(result))

# 결과 출력
sys.stdout.write("\n".join(results))