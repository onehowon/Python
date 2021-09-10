num = [] # 빈 리스트 형성
count_p = 0 
count_m = 0

for i in range(5): # 입력할 숫자를 5번 넣을 때까지 반복
    number=int(input("%d. 숫자를 입력하세요" %(i+1)))
    num.append(number) # 사용자가 입력한 숫자가 리스트에 추가됨

for i in range(5): # 양수인지 음수인지 개수를 세기 위한 반복문
    if num[i] > 0: # 0보다 클 경우 양수이므로 양수 카운트 증가
        count_p = count_p + 1
    elif num[i] < 0: # 0보다 작을 경우 음수이므로 음수 카운트 증가
        count_m = count_m + 1

print("양의 정수는 ", count_p, "음의 정수는", count_m)