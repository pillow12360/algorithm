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
        print(num)

    def empty(self):
        if self.head is None:
            print(1)
        else:
            print(0)

    def pop(self):
        if self.head is not None:
            current = self.head
            print(current.value)
            self.head = current.next

        else:
            print(-1)

    def front(self):
        if self.head is not None:
            current = self.head
            print(current.value)
        else:
            print(-1)

    def back(self):
        if self.head is not None:
            current = self.head
            while current.next:
                current = current.next
            print(current.value)
        else:
            print(-1)

def stackfunc(A, B, stack):
    if A == "push":
        stack.push(B)
    elif A == "pop":
        stack.pop()
    elif A == "empty":
        stack.empty()
    elif A == "front":
        stack.front()
    elif A == "size":
        stack.size()
    elif A == "back":
        stack.back()

num = int(input())

ll = LinkedList()

while num > 0:
    C = input()
    if " " in C:
        A, B = C.split()
    else:
        A = C
        B = None
    stackfunc(A, B, ll)
    num -= 1
