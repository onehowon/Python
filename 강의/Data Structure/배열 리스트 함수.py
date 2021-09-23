items = [] # 리스트 항목 저장을 위한 파이썬 리스트
def insert(pos,elem): # pos 위치에 새로운 요소 item을 삽입한다.
    items.insert(pos,elem) # 파이썬 리스트 클래스의 insert 연산
def delete(pos): # pos 위치에 있는 요소를 꺼내고 반환한다.
    return items.pop(pos) # 파이썬 리스트 클래스의 POP 연산
def getEntry(pos): return items[pos] # pos번째 항목 반환
def isEmpty(): return len(items) ==0 # 크기가 0이면 True 아니면 False
def size(): return len(items) # 리스트의 크기 반환. len() 함수 이용
def clear(): items = [] # items를 초기화 --> 오류
def find(item): return items.index(item) # 탐색 후 인덱스 반환
def replace(pos, elem): items[pos] = elem # pos번째 항목 변경
def sort(): items.sort() #정렬(sort 메소드 이용)
def merge(lst): items.extend(lst) #병합(확장)
def display(msg='ArrayList: '): #출력: 디폴트 인수 사용
    print(msg, size(), items) #메시지+크기+배열내용 출력

display('파이썬 리스트로 구현한 리스트 테스트')
insert(0, 10);insert(0,20);insert(1,30)
insert(size(), 40);insert(2,50)
display("파이썬 리스트로 구현한 List(삽입x5): ")
sort()
display("파이썬 리스트로 구현한 List(정렬후): ")
replace(2,90)
display("파이썬 리스트로 구현한 List(교체x1): ")
delete(2); delete(size() -1); delete(0)

display("파이썬 리스트로 구현한 List(삭제x3): ")
lst = [1,2,3]
merge(lst)
display("파이썬 리스트로 구현한 List(병합): ")
clear()
display("파이썬 리스트로 구현한 List(정리후)")