class Node:
    def __init__(self, key, value, height, left=None, right=None):
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right

class AVL:
    def __init__(self):
        self.root = None

    def height(self, n):
        if n == None:
            return 0
        return n.height
        
    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)
    
    def put_item(self, n, key, value):
        if n == None:
            return Node(key, value, 1)
    
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        else:
            n.value = value
            return n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)
    
    def balance(self, n): # 불균형 처리
        if self.bf(n) > 1:
            if self.bf(n.left) < 0:
                n.left = self.rotate_left(n.left)
            n = self.rotate_right(n)
    
        elif self.bf(n) < -1:
            if self.bf(n.right) > 0:
                n.right = self.rotate_right(n.right)
            n = self.rotate_left(n)
        return n

    def bf(self, n): # 계산
        return self.height(n.left) - self.height(n.right)

    def rotate_right(self, n): # 우로 회전
        x = n.left
        n.left = x.right
        x.right = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x
    def rotate_left(self, n): # 좌로 회전
        x = n.right
        n.right = x.left
        x.left = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def delete(self,key):
        self.root = self.delete_node(self.root,key)

    def delete_node(self,n,key):
        if n == None:
            return None
        if n.key > key:
            n.left = self.delete_node(n.left,key)
        elif n.key < key:
            n.right = self.delete_node(n.right, key)
        else:
            if n.right == None:
                return n.left
            if n.left == None:
                return n.right
            target = n
            n = self.minimum(target.right)
            n.right = self.del_min(target.right)
            n.left = target.left
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def delete_min(self):
        if self.root == None:
            print("트리가 비어 있음.")
        self.root = self.del_min(self.root)

    def del_min(self,n):
        if n.left == None:
            return n.right
        n.left = self.del_min(n.left)
        n.height = max(self.height(n.left), self.height(n.right))+1
        return self.balance(n)
    
    def min(self):
        if self.root == None:
            return None
        return self.minimum(self.root)

    def minimum(self, n):
        if n.left == None:
            return n
        return self.minimum(n.left)

    def preorder(self,n):
        print(str(n.key), ' ', end='')
        if n.left:
            self.preorder(n.left)
        if n.right:
            self.preorder(n.right)

    def inorder(self,n):
        if n.left:
            self.inorder(n.left)
        print(str(n.key), ' ', end='')
        if n.right:
            self.inorder(n.right)
