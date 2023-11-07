class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return

        val = self.head
        while val.next is not None:
            val = val.next
        val.next = node

    def pprint(self):
        temp:Node = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print()

data = LinkedList()
# breakpoint()
data.append(10)
data.append(20)
data.append(30)
data.pprint()
