number = [] # 빈 리스트 형성
for i in range(1,9,3): # 1부터 9까지 3씩 증가하는 숫자들의 반복
    small_list = [] # 리스트 초기화
    for j in range(3): #0부터 2까지 3개의 숫자들에 대해 반복
        small_list.append(i+j) # 리스트에 요소 추가
    number.append(small_list) # 만들어진 작은 리스트들 number 리스트에 추가
print(number)


