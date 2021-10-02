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
    def checkBrackets(statement):
        stack = Stack()
        for ch in statement: # 문자열의 각 문자에 대해
            if ch in ('{', '[', '('): # in '{[('도 동일하게 동작함
                stack.push(ch)
            elif ch in ('}', ']', ')'): # in '}])'도 동일하게 동작함
                if stack.isEmpty():
                    return False # 조건 2 위반
                else:
                    left = stack.pop()
                    if(ch == "}" and left != "{") or \
                        (ch == "]" and left != "[") or \
                            (ch == ")" and left != "("):
                            return False # 조건 3 위반
        return stack.isEmpty() # False 이면 조건 1 위반
    str = ( " { A[(i+1] = 0; }", "if ( ( i==0) && (j==0)", "A[ (i+1]) =0;")
    for s in str:
        m = checkBrackets(s)
        print(s, " ---> ", m)
    