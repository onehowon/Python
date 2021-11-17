class Chaining:
    class Node:
        def __init__(self,key,data,link):
            self.key = key
            self.data = data
            self.next = link
    def __init__(self,size):
        self.M = size
        self.a = [None] * size
    
    def hash(self,key):
        return key % self.M
    
    def put(self, key, data):
        i = self.hash(key)
        p = self.a[i]
        while p != None:
            if key == p.key:
                p.data = data
                return
            p = p.next
        self.a[i] = self.Node(key, data, self.a[i])

    def get(self, key):
        i = self.hash(key)
        p = self.a[i]
        while p != None:
            if key == p.key:
                return p.data
            p = p.next
        return None
    
    def print_table(self):
        for i in range(self.M):
            print('%2d' % (i), end='')
            p = self.a[i];
            while p != None:
                print('-->[', p.key, ',', p.data, ']', end='')
                p = p.next
            print()