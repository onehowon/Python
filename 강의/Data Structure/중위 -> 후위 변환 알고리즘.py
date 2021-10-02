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
    def precedence(op):
        if op == '(' or op ==')' : return 0
        elif op =='+' or op =='-' : return 1
        elif op == '*' or op =='/' : return 2
        else : return -1
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
    def Infix2Postfix(expr): # expr : 입력 리스트(중위 표기식)
        s = Stack()
        output = [] # output : 출력 리스트(후위 표기식)
        for term in expr:
            if term in '(': # 왼쪽 괄호 삽입이면
                s.push('(') # 스택에 삽입
            elif term in ')': # 오른쪽 괄호이면
                while not s.isEmpty():
                    op = s.pop()
                    if op =='(' : break; # 왼쪽 괄호가 나올 때까지
                    else: # 스택에서 연산자를 꺼내 출력
                        output.append(op)
            elif term in "+-*/": # 연산자이면
                while not s.isEmpty(): # 우선순위가 높거나 같은 연산자를
                    op = s.peek() # 스택에서 모두꺼내 출력
                    if(precedence(term) <= precedence(op)):
                        output.append(op)
                        s.pop()
                    else: break
                s.push(term) # 마지막으로 현재 연산자 삽입
            else: # 피연산자이면
                output.append(term) # 바로 출력
        while not s.isEmpty(): # 처리가 끝났으면 스택에 남은 항목을
            output.append(s.pop()) # 모두 출력
        return output # 결과
    infix1 = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
    infix2 = ['1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']
    postfix1 = Infix2Postfix(infix1)
    postfix2 = Infix2Postfix(infix2)
    result1 = evalPostfix(postfix1)
    result2 = evalPostfix(postfix2)
    print('중위표기: ', infix1)
    print('후위표기', postfix1)
    print('계산결과', result1, end='\n\n')
    print('중위표기', infix2)
    print('후위표기', postfix2)
    print('계산결과', result2)