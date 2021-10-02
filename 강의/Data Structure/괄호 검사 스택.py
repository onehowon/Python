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
    def evalPostfix(expr):
        s = Stack() # 스택 객체 생성
        for token in expr: # 리스트의 모든 항목에 대해
            if token in "+-*/": # 항목이 피연산자이면
                val2 = s.pop() # 피연산자2
                val1 = s.pop() # 피연산자 1
                if(token == '+'): s.push(val1 + val2) # 각 연산 수행
                elif(token == '-'): s.push(val1 - val2) # 결과는 스택에
                elif(token == '*'): s.push(val1 * val2) # 다시 저장
                elif(token == '/'): s.push(val1 / val2)
            else: # 항목이 피연산자이면
                s.push(float(token)) # 실수로 변경해서 스택에 저장
            return(s.pop()) # 최종 결과를 반환
    expr1 = ['8', '2','/','3','-','3','2','*','+']
    expr2 = ['1','2','/','4','*','1','4','/','*']
    print(expr1, '-->', evalPostfix(expr1))
    print(expr2, '-->', evalPostfix(expr2))
