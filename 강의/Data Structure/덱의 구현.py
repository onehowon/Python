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
            out = self.items[self.front+1:Max_QSIZE] + self.items[0:self.rear+1] # 슬라이싱
        print("[f=%s,r=%d] ==> "%(self.front, self.rear), out)
    def clear(self): self.top = [] # 주의 : 이제 전역변수 선언이 필요없다.
    def push(self, item):
        self.top.append(item)
        
class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()

    def addRear(self,item): self.enqueue(item)
    def deleteFront(self): return self.dequeue()
    def getFront(self): return self.peek()
    def addFront(self,item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = self.front - 1 # 반시계 방향으로 회전
            if self.front < 0 : self.front = Max_QSIZE - 1

    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear];
            self.rear = self.rear - 1
            if self.rear < 0 : self.rear = Max_QSIZE - 1
            return item
    def getRear(self):
        return self.items[self.rear]
dq = CircularDeque()
for i in range(9):
    if i%2 == 0: dq.addRear(i)
    else: dq.addFront(i)
dq.display()
for i in range(2): dq.deleteFront()
for i in range(3): dq.deleteRear()
dq.display()
for i in range(9,14): dq.addFront(i)
dq.display()

class PriorityQueue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def size(self): return len(self.items)
    def clear(self): self.items = []
    def enqueue(self,item):
        self.items.append(item)
    def findMaxIndex(self):
        if self.isEmpty(): return None
        else:
            highest = 0
            for i in range(1, self.size()):
                if self.items[i] > self.items[highest]:
                    highest = i
            return highest
    def dequeue(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items.pop(highest)
    def peek(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items[highest]
q = PriorityQueue()
q.enqueue(34)
q.enqueue(18)
q.enqueue(27)
q.enqueue(45)
q.enqueue(15)

print("PQueue:", q.items)
while not q.isEmpty():
    print("Max Priority = ", q.dequeue())

import math
(ox,oy) = (5,4)
def dist(x,y):
    (dx, dy) = (ox-x, oy-y)
    return math.sqrt(dx*dx + dy*dy)

    
    def findMaxIndex(self):
        if self.isEmpty(): return None
        else:
            highest = 0
            for i in range(1, self.size()):
                if self.items[i][2] > self.items[highest][2]:
                    highest = i
                return highest
def isValidPos(x,y):
    if x < 0 or y <0 or x >=MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'
def MySmartSearch():
    q = PriorityQueue()
    q.enqueue((0,1,-dist(0,1)))
    print('PQueue: ')

    while not q.isEmpty():
        here = q.dequeue()
        print(here[0:2], end='->')
        x,y,_ = here
        if(map[y][x] == 'x'): return True
        else:
            map[y][x] ='.'
            if isValidPos(x,y-1): q.enqueue((x,y-1, -dist(x,y-1)))
            if isValidPos(x,y+1): q.enqueue((x,y+1, -dist(x,y+1)))
            if isValidPos(x-1,y): q.enqueue((x-1,y, -dist(x-1,y)))
            if isValidPos(x+1,y): q.enqueue((x+1,y, -dist(x+1,y)))
        print('우선순위큐: ', q.items)
    return False
map = [[ '1','1','1','1','1','1'],
    ['e','0','1','0','0','1'],
    ['1','0','0','0','1','1'],
    ['1','0','1','0','1','1'],
    ['1','0','1','0','0','x'],
    ['1','1','1','1','1','1']]
MAZE_SIZE = 6
result = MySmartSearch()
if result : print(' --> 미로탐색 성공')
else: print(' --> 미로탐색 실패')