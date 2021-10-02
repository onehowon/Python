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
            self.items[self.front] # front 위치의 항목 반환
    def peek(self):
        if not self.isEmpty():
            return self.itmes[(self.front + 1) % Max_QSIZE]
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
q = CircularQueue() # 원형 큐 만들기
for i in range(8): q.enqueue(i) # 0,1, ... 7 삽입(f=0, r=8)
q.display() # 원형 큐에서 구현한 print() 호출
for i in range(5): q.dequeue(); # 5번 삭제(f=5, r=8)
q.display()
for i in range(8,14): q.enqueue(i) # 8,9, ... 13 삽입(f=5, r=4)
q.display

    #### 너비우선탐색 알고리즘 ####
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
                if isValidPos(x,y-1): que.enqueue((x,y-1)) # 상
                if isValidPos(x,y+1): que.enqueue((x,y+1)) # 하
                if isValidPos(x-1,y): que.enqueue((x-1,y)) # 좌
                if isValidPos(x+1,y): que.enqueue((x+1,y)) # 우
            return False
    map = [[ '1','1','1','1','1','1'],
    ['e','0','0','0','0','1'],
    ['1','0','1','0','1','1'],
    ['1','1','1','0','0','x'],
    ['1','1','1','0','1','1'],
    ['1','1','1','1','1','1']]
    MAZE_SIZE = 6
    result = BFS()
    if result : print(' --> 미로탐색 성공')
    else: print(' --> 미로탐색 실패')
