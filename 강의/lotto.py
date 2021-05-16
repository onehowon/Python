### 로또 번호 자동 생성기 프로그램
## PY#1_202021524_성원호
# 난수 추출 모듈인 random 사용
import random
qty = int(input("구매할 로또의 개수를 입력하세요: ")) # 몇장의 로또를 구매할지 input문을 통해 입력 값에 따라 로또 번호가 나오도록 만든다.

for i in range(qty): # 사용자가 입력한 범위까지(로또 구매 장수)를 추출하기 위함
    lotto_list = [0, 0, 0, 0, 0, 0] # 기본적인 로또 번호는 6자리이므로 6개의 숫자 리스트를 만들어준다.
    lotto_bonus = [0] # 보너스 번호의 리스트
    for j in range(6): # 6개의 로또 번호까지의 범위를 추출하기 위함
        number = 0 # 난수 추출을 위한 임의의 변수 지정
        while(number in lotto_list): # while문을 통해 lotto_list라는 변수명의 리스트에 number 값이 포함된다라는 가정이 True일 경우까지 반복하는 조건식을 생성해준다.
            # 또한 로또 번호에 있어 중복된 숫자가 나오면 안되기 때문에 중복 숫자를 피하기 위해서도 만들어진 조건식이다.
            number = random.randint(1, 45) # 변수 number의 범위는 1부터 45까지로, 임의의 난수를 추출하는 randint 함수를 사용한다.
        lotto_list[j] = number # 추출된 6개의 번호들을 lotto_list에 저장한다.
    for x in range(1): # 1개의 보너스 번호 추출을 위해 범위 지정
        while True: # while True문인 무한 루프 통해 6개의 기본 번호와 겹치지 않도록 조건식을 설정해준다.
            bonus_number = random.randint(1, 45) # 보너스 번호도 마찬가지로 1부터 45 사이의 임의의 난수를 하나 추출한다.
            if bonus_number not in lotto_list: # 보너스 번호가 6개의 기본 번호 리스트 안에 없다면이라는 가정문을 생성한다.
                lotto_bonus[x] = bonus_number # 없을 경우 보너스 번호 리스트에 추가한다.
                break # 중복일 경우 무한루프로, 중복이 아닐 때 종료한다.
        print(i+1, "번 로또:",sorted(lotto_list), "보너스 번호는:",lotto_bonus) # 로또를 n장 구매했을 경우에 "n번 로또"의 형태로 출력해야 하기 때문에 for 문의 i에서 +1을 더한 것을 순서로 나타내는데 사용한다.
        # sorted 함수를 통해 낮은 번호부터 높은 번호 순서대로 출력하게 만든다.
        # 출력 결과 "n번 로또" : [], "보너스 번호는" : [] 의 형태로 출력되는 것을 확인하였다.

