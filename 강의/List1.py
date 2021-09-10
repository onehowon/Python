num = [] #  숫자 5개를 할당할 리스트를 생성
sum = 0
for i in range(5): # 숫자가 5개이므로 5개를 뽑을 때까지 반복
    newnum = int(input("%d번 숫자를 입력하세요 : " %(i+1)))
    num.append(newnum) # 입력한 숫자에 기반해 수를 추가함
for i in range(5):
    sum = sum + num[i] # 추가를 5번 반복한다.

print("숫자의 합계는", sum, "입니다")
