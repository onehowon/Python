class DoubleHashing:
    def __init__(self,size):
        self.M = size # 테이블 크기
        self.a = [None] * size # 해시테이블 a
        self.d = [None] * size # 데이터 저장용 d
        self.N = 0 # 저장된 항목 수 N

    def hash(self,key):
        return key % self.M

    def put(self,key, data):
        initial_position = self.hash(key) # 초기 위치
        i = initial_position
        d = 7 - (key % 7)
        j = 0
        while True:
            if self.a[i] == None: # 빈곳 발견
                self.a[i] = key # key는 해시테이블에
                self.d[i] = data # data는 리스트 d에 저장
                self.N +=1
                return
            if self.a[i] == key: # key가 이미 해시 테이블에 있으면
                self.d[i] = data # data만 갱신
                return
            j += 1
            i = (initial_position + j*d) % self.M # 다음 원소 검사를 위해
            if self.N > self.M: # 다음 위치가 초기 위치와 같다면 루프 벗어나기[저장 실패]
                break
    def print_table(self): # 해시 테이블 출력
        for i in range(self.M):
            print('{:4}'.format(str(i)), ' ', end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])), ' ', end ='')
        print()
    
    def get(self, key):
        initial_position = self.hash(key) # 초기 위치
        i = initial_position
        d = 7 - (key % 7)
        j = 0
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]
            i = (initial_position + j*d) % self.M
            j += 1
        return None