class Stack:
    def __init__(self): # 생성자
        self.top = [] # top이 이제 클래스의 멤버 변수가 됨
    def isEmpty(self): return len(self.top) == 0
    def size(self): return len(self.top)
    def clear(self): self.top = [] # 주의 : 이제 전역변수 선언이 필요없다.
    def push(self, item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
odd = Stack() # 홀수 스택
even = Stack() # 짝수 스택
for i in range(10):
    if i%2 ==0 : even.push(i) # 짝수는 even에
    else : odd.push(i) # 홀수는 odd에 push
    def isValidPos(x,y):
        if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
            return False
        else:
            return map[y][x] == '0' or map[y][x] =='x' 
    def DFS(): # 깊이 우선 탐색 함수
        stack = Stack() # 사용할 스택 객체를 준비
        stack.push((0,1)) # 시작위치 삽입. (0,1)은 튜플
        print('DFS:')

        while not stack.isEmpty(): # 공백이 아닐 동안
            here = stack.pop() # 항목을 꺼냄(pop)
            print(here, end='->')
            (x,y) = here # 스택에 저장된 튜플은 (x,y) 순서임
            if(map[y][x] == 'x'):  # 출구이면 탐색 성공. True 반환
                return True
            else:
                map[y][x] == '.' # 현재 위치를 지나왔다고 '.' 표시
                if isValidPos(x,y -1): stack.push((x,y -1)) # 상
                if isValidPos(x,y +1): stack.push((x,y +1)) # 하
                if isValidPos(x -1, y): stack.push((x-1, y)) # 좌
                if isValidPos(x + 1, y): stack.push((x+1, y)) # 우
            print("현재 스택: ", stack) # 현재 스택 내용 출력
        return False # 탐색 실패. False 반환
    map = [[ '1','1','1','1','1','1'],
    ['e','0','1','0','0','1'],
    ['1','0','0','0','1','1'],
    ['1','0','1','0','1','1'],
    ['1','0','1','0','0','x'],
    ['1','1','1','1','1','1']]
    MAZE_SIZE = 6
    result = DFS()
    if result : print(' --> 미로탐색 성공')
    else: print(' --> 미로탐색 실패')
