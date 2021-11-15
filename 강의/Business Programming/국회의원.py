import math

A = int(input("A 정당의 지역구 의석 수를 입력하십시오: "))
B = int(input("B 정당의 지역구 의석 수를 입력하십시오: "))
C = int(input("C 정당의 지역구 의석 수를 입력하십시오: "))
D = int(input("D 정당의 지역구 의석 수를 입력하십시오: "))

A_per = float(input("A 정당의 지지율을 입력해주세요: "))
B_per = float(input("B 정당의 지지율을 입력해주세요: "))
C_per = float(input("C 정당의 지지율을 입력해주세요: "))
D_per = float(input("D 정당의 지지율을 입력해주세요: "))

localseat = [A,B,C,D]
percentage = [A_per,B_per,C_per,D_per]

def semi(seat,per): # 준연동형
    Total = 300
    calc = ((Total * (per/100) - seat)) / 2
    if calc < 0:
        calc = 0
    return calc

def parallel(per): # 병립형
    Total = 17
    parallel_seat = round(Total * (per / 100))
    if parallel_seat < 0:
        parallel_seat = 0
    return parallel_seat

parallel_seat = []
semi_seat = []
total_seat = []

semi_seat.append(localseat, percentage)
semi_sum = semi_seat[0] + semi_seat[1] + semi_seat[2] + semi_seat[3]
print(semi_seat)
print(semi_sum)
