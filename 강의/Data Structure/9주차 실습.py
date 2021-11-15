class TNode:
    def __init__ (self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def preorder(n):
    if n is not None :
        print(n.data,end=' ')
        preorder(n.left)
        preorder(n.right)

def inorder(n): # 전위순회 함수
    if n is not None:
        inorder(n.left) # 왼쪽 서브트리 처리
        print(n.data, end= ' ') # 루트노드 처리(화면 출력)
        inorder(n.right) #오른쪽 서브트리 처리

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')
Max_QSIZE = 10 # 원형 큐의 크기
class CircularQueue:
    def __init__(self): # circularQueue 생성자
        self.front = 0  # 큐의 전단 위치
        self.rear = 0 # 큐의 후단 위치
        self.items = [None] * Max_QSIZE # 항목 저장 리스트
    def isEmpty(self): return self.front == self.rear
    def isFull(self): return self.front == (self.rear+1)%Max_QSIZE
    def clear(self): self.front = self.rear
    def enqueue(self,item):
        if not self.isFull(): #포화 상태가 아니라면
            self.rear = (self.rear+1) % Max_QSIZE # rear 회전
            self.items[self.rear] = item # rear 위치에 삽입
    #### 원형 큐의 연산들(삽입 / 삭제) ####
    def dequeue(self):
        if not self.isEmpty(): # 공백 상태가 아니라면
            self.front = (self.front+1) % Max_QSIZE # front 회전
            return self.items[self.front] # front 위치의 항목 반환
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % Max_QSIZE]
    def size(self):
        return(self.rear - self.front + Max_QSIZE) % Max_QSIZE
    #### 원형 큐의 연산들 (출력) ####
    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1] # 슬라이싱
        else:
            out = self.items[self.front+1:Max_QSIZE]\
            + self.items[0:self.rear+1] # 슬라이싱
        print("[f=%s,r=%d] ==> "%(self.front, self.rear), out)
  
def isValidPos(x,y):
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] =='x' 
def BFS():
    que = CircularQueue()
    que.enqueue((0,1))
    print('BFS: ') # 출력을 BFS로 변경

    while not que.isEmpty():
        here = que.dequeue()
        print(here, end='->')
        x,y = here
        if(map[y][x] == 'x'): return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y-1): que.enqueue((x, y-1)) # 상
            if isValidPos(x, y+1): que.enqueue((x, y+1)) # 하
            if isValidPos(x-1, y): que.enqueue((x-1, y)) # 좌
            if isValidPos(x+1, y): que.enqueue((x+1, y)) # 우
    return False
map = [[ '1','1','1','1','1','1'],
    ['e','0','1','0','0','1'],
    ['1','0','0','0','1','1'],
    ['1','0','1','0','1','1'],
    ['1','0','1','0','0','x'],
    ['1','1','1','1','1','1']]
MAZE_SIZE = 6
result = BFS()
if result : print(' --> 미로탐색 성공')
else: print(' --> 미로탐색 실패')

def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end= ' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)
def count_node(n): # 순환을 이용해 트리의 노드 수를 계산하는 함수
    if n is None: # n이 None이면 공백 트리 --> 0을 반환
        return 0
    else: # 좌우 서브트리의 노드수의 합 +1을 반환(순환이용)
        return 1 + count_node(n.left) + count_node(n.right)
def count_leaf(n):
    if n is None: # 공백 트리 --> 0을 반환
        return 0
    elif n.left is None and n.right is None: # 단말노드 --> 1을 반환
        return 1
    else:  # 비단말 노드 : 좌우 서브트리의 결과 합을 반환
        return count_leaf(n.left) + count_leaf(n.right)
def calc_height(n):
    if n is None: # 공백 트리 --> 0을 반환
        return 0
    hLeft = calc_height(n.left) # 왼쪽 트리의 높이 --> hLeft 
    hRight = calc_height(n.right) # 오른쪽 트리의 높이 --> hRight
    if (hLeft > hRight): # 더 높은 높이에 1을 더해 반환
        return hLeft + 1
    else:
        return hRight + 1
    

d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
f = TNode('F', None, None)
c = TNode('C',f, None)
root = TNode('A',b, c)


print('\n In-Order : ', end='')
inorder(root)
print('\n Pre-order : ', end='')
preorder(root)
print('\n Post-Order : ', end='')
postorder(root)
print('\nLevel-Order : ', end='')
levelorder(root)
print()

print("노드의 개수 = %d개"% count_node(root))
print("단말의 개수 = %d개"% count_leaf(root))
print("트리의 높이 = %d개"% calc_height(root))
#-------------------------------------------#
class TNode:
    def __init__ (self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

table = [('A','.-'),    ('B', '-...'),  ('C','-.-.'),   ('D','-..'),
('E','.'),  ('F','..-.'),   ('G','--.'),    ('H', '....'),
('I', '..'),    ('J','.---'),   ('K','-.-'),    ('L', '.-..'),
('M', '--'),    ('N','-.'),    ('O','---'), ('P', '.--.'),
('Q','--.-'),   ('R','.-.'),    ('S', '...'),   ('T', '-'),
('U', '..-'),   ('V', '...-'),  ('W','.--'),    ('X','-..-'),
('Y','-.--'),   ('Z', '--..')]

def make_morse_tree():
        root = TNode(None, None, None)
        for tp in table:
            code = tp[1]
            node = root
            for c in code:
                if c == '.':
                    if node.left == None:
                        node.left = TNode(None,None,None)
                    node = node.left
                elif c == '-':
                    if node.right == None:
                        node.right = TNode(None,None,None)
                    node = node.right
            node.data = tp[0]
        return root
def decode(root, code):
    node = root
    for c in code:
        if c == '.' : node = node.left
        elif c == '-': node =node.right
    return node.data

def encode(ch):
    idx = ord(ch)-ord('A')
    return table[idx][1]

morseCodeTree = make_morse_tree()
str = input("입력 문장 : ")
mlist = []
for ch in str:
  code = encode(ch)
  mlist.append(code)

print("Morse Code: ", mlist)
print("Decoding : ", end = '')
for code in mlist:
  ch = decode(morseCodeTree, code)
  print(ch, end='')
print()