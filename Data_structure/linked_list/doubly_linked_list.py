class Node:
    def __init__(self, data):
        self.data  = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, data):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        
    def pprint(self):
        ...