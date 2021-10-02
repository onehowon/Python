top = [] # 스택의 데이터 : 항목을 위한 공백 리스트
def isEmpty():
    return len(top) == 0 # len(top) == 0 의 계산 결과가 True/False
def push(item):
    top.append(item) # 리스트의 맨 뒤에 item을 추가함
def pop():
    if not isEmpty(): # 공백상태가 아니면
        return top.pop(-1) # 리스트의 맨 뒤에서 항목을 하나 꺼내고 반환
def peek(): # 맨 위의 항목을 삭제하지 않고 반환
    if not isEmpty(): # 공백 상태가 아니면
        return top[-1] # 맨 뒷 항목을 반환(삭제하지 않음)
def size(): return len(top) # 스택의 크기
def clear():
    global top # top은 전역변수임을 지정함
    top = [] # 스택의 초기화
    

for i in range(1,6):
    push(i) # push 연산 5회
print(' push 5회: ', top) # 스택 내용 출력
print(' pop() --> ', pop()) # pop연산 및 반환 항목 출력
print(' pop() --> ', pop()) # pop연산 및 반환 항목 출력
print(' pop 2회: ', top) # 스택 내용 출력