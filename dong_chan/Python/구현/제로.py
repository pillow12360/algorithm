class node():
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,value):
        new_node = node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def pop(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.tail
            self.tail = current.prev
            self.tail.next = None


    def get(self):
        currunt = self.head
        while currunt:
          print(currunt.value)
          currunt = currunt.next

    def hap(self):
        hap = 0

        if self.head is None:
            print(hap)
        else:
          currunt = self.head
          while currunt is not None:
            hap += currunt.value
            currunt = currunt.next
          print(hap)

# num = int(input())
ll = LinkedList()



num = int(input())

while num>0:
    innum = int(input())
    if innum == 0:
        ll.pop()
    else:
        ll.append(innum)
    num -= 1

ll.hap()
    
