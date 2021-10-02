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
print(' 스택 even push 5회: ', even) # even stack 출력
print(' 스택 odd push 5회: ', odd) # odd stack 출력
print(' 스택 even   peek:', even.peek()) # even 스택 peek()
print(' 스택 odd    peek:', odd.peek()) # odd 스택 peek()
for _ in range(2) : even.pop() # even 스택에서 두번 pop()
for _ in range(3) : odd.pop() # odd 스택에서 세번 pop()
print(' 스택 even   pop 2회:', even.top)
print(' 스택 odd    pop 3회:', odd.top)
