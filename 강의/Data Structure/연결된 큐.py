class Node:
    def __init__ (self, elem, link = None):
        self.data = elem
        self.link = link


class LinkedStack:
    def __init__ (self):
        self.top = None

    def isEmpty(self): return self.top ==  None
    def clear(self): self.top = None
    def push(self, item):
        n = Node(item, self.top)
        self.top = n
    
    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data
    def peek(self):
        if not self.isEmpty():
            return self.top.data

    def size(self):
        node = self.top
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count
    def display(self, msg='LinkedStack:'):
        print(msg, end='')
        node = self.top
        while not node == None:
            print(node.data, end=' ')
            node = node.link
        print()

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self): return self.head == None
    def clear(self): self.head = None
    def size(self):
        node = self.head
        count = 0
        while not node == None:
            node = node.link
            count += 1
    def display(self, msg=  'LinkedList: '):
        print(msg, end = '')
        node = self.head
        while not node == None:
            print(node.data, end=' ')
            node = node.link
        print()
    def getNode(self, pos):
        if pos < 0: return Node
        node = self.head;
        while pos >0 and node != None:
            node = node.link
            pos -= 1
        return node
    
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None: return None
        else : return node.data

    def replace(self, pos, elem):
        node = self.getNode(pos)
        if node != None: node.data = elem

    def find(self, data):
        node = self.head;
        while node is not None:
            if node.data == data : return node
            node = node.link
        return node
    
    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.link)
            before.link = node
    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link

class CircularLinkedQueue:
    def __init__(self):
        self.tail = None
    
    def isEmpty(self): return self.tail == None
    def clear(self): self.tail = None
    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data
    def enqueue(self, item):
        node = Node(item, None)
        if self.isEmpty():
            node.link = node
            self.tail = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node
    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail:
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data
    def size(self):
        if self.isEmpty(): return 0
        else:
            count = 1
            node = self.tail.link
            while not node == self.tail:
                node =node.link
                count += 1
            return count
    def display(self, msg = 'CircularLinkedQueue: '):
        print(msg, end='')
        if not self.isEmpty():
            node = self.tail.link
            while not node == self.tail:
                print(node.data, end=' ')
                node = node.link
            print(node.data, end=' ')
        print()

q = CircularLinkedQueue()
for i in range(8): q.enqueue(i)
q.display()
for i in range(5): q.enqueue(i)
q.display()
for i in range(8,14): q.enqueue(i)
q.display()