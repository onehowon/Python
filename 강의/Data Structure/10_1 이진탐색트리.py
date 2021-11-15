class BSTNode: # 이진 탐색트리를 위한 노드 클래스
    def __init__ (self, key, value): # 생성자 : 키와 값을 받음
        self.key = key # 키 (key)
        self.value = value # 값 (value)
        self.left = None # 왼쪽 자식에 대한 링크
        self.right = None # 오른쪽 자식에 대한 링크

# 이진탐색트리 탐색연산(순환 함수)
def search_bst(n,key):
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)
    
def search_bst_iter(n, key):
    while n != None:
        if key == n.key:
            return n
        elif key < n.key:
            n = n.left
        else:
            n = n.right
    return None

def search_max_bst(n): # 최대 값의 노드 탐색
    while n != None and n.right != None:
        n = n.right
    return n

def search_min_bst(n): # 최소 값의 노드 탐색
    while n != None and n.left != None:
        n = n.left
    return n

# 이진탐색트리 삽입연산(노드를 삽입함): 순환구조 이용
def insert_bst(r,n):
    if n.key < r.key: # 삽입할 노드의 키가 루트보다 작으면
        if r.left is None: # 루트의 왼쪽 자식이 없으면
            r.left = n # n은 루트의 왼쪽 자식이 됨.
            return True
        else: # 루트의 왼쪽 자식이 있으면
            return insert_bst(r.left, n) # 왼쪽 자식에게 삽입하도록 함
    elif n.key > r.key: # 삽입할 노드의 키가 루트보다 크면
        if r.right is None: # 루트의 오른쪽 자식이 없으면
            r.right = n # n은 루트의 오른쪽 자식이 됨.
            return True
        else: # 루트의 오른쪽 자식이 있으면
            return insert_bst(r.right, n) # 오른쪽 자식에게 삽입하도록 함
    else: # 키가 중복되면
        return False # 삽입하지 않음
    
def delete_bst_case1(parent, node, root):
    if parent is None: # 삭제할 단말 노드가 루트이면
        root = None # 공백 트리가 됨
    else:
        if parent.left == node: # 삭제할 노드가 부모의 왼쪽 자식이면
            parent.left = None # 부모의 왼쪽 링크를 None
        else: # 오른쪽 자식이면
            parent.right = None # 부모의 오른쪽 링크를 None

    return root # root가 변경될 수도 있으므로 반환
    
def delete_bst_case2(parent, node, root):
    if node.left is not None:
        child = node.left
    else:
        child = node.right
        
    if node == root:
        root = child
    else:
        if node is parent.left:
            parent.left = child
        else:
            parent.right = child
    return root

    #삭제 알고리즘
def delete_bst_case3(parent, node, root):
    succp = node # 후계자의 부모 노드
    succ = node.right # 후계자 노드
    while (succ.left != None): # 후계자와 부모노드 탐색
        succp = succ 
        succ = succ.left

    if(succp.left == succ): # 후계자가 왼쪽 자식이면
        succp.left = succ.right # 후계자의 오른쪽 자식 연결
    else: # 후계자가 오른쪽 자식이면
        succp.right = succ.right # 후계자의 왼쪽 자식 연결
    node.key = succ.key # 후계자의 키와 값을
    node.value = succ.value # 삭제할 노드에 복사
    node = succ; # 실제로 삭제하는 것은 후계자 노드

    return root;

def delete_bst(root,key):
    if root == None: return None # 공백 트리

    parent = None # 삭제할 노드 부모 탐색
    node = root # 삭제할 노드 탐색
    while node != None and node.key != key: # parent 탐색
        parent = node
        if key < node.key : node = node.left
        else: node = node.right;

    