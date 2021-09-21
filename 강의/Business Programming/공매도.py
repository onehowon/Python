import pandas as pd
import numpy as np 

### 네이버 증권 기준
# 한국 3월 9일부터 13일까지의 코스피 지수
# 3/9 1947, 1990 / 1935,1968 / 1898,1968 / 1809, 1897 / 1681, 1809

# 미국 3월 9일부터 13일까지의 다우존스 지수
# 3/9 23,706, 24,922 / 23,690 ,25,020 / 23,328, 24,604 / 21,154, 22,837 / 21,285, 23,189 

#### 1번 Guide Line ####
# 3월 9일부터 15일까지의 코스피 지수
kor_mi = list(map(int,input("3월 9일부터 13일까지의 한국 코스피 지수의 최고점을 5개 입력하세요.>").split()))
kor_ma = list(map(int,input("3월 9일부터 13일까지의 한국 코스피 지수의 최저점을 5개 입력하세요.>").split()))
us_mi = list(map(int,input("3월 9일부터 13일까지의 미국 다우존스 지수의 최고점을 5개 입력하세요.>").split()))
us_ma = list(map(int,input("3월 9일부터 13일까지의 미국 다우존스 지수의 최저점을 5개 입력하세요.>").split()))

#### 2번 Guide Line ####
### 변동폭 계산 최고점 - 최저점
### 변동폭의 백분율 계산 (최고점 - 최저점) / 최저점 * 100
# 한국의 Daily 변동폭을 입력할 빈 리스트 형성
kor_rate = []
# 코스피 변동률 계산
def kor(a):
    b = kor_ma[a] - kor_mi[a]
    c = (kor_ma[a] - kor_mi[a]) / kor_mi[a] * 100
    return b,c

# 변동률을 리스트에 추가하여 출력
kor_rate.append(kor(1))
kor_rate.append(kor(2))
kor_rate.append(kor(3))
kor_rate.append(kor(4))
print("코스피의 일일 변동폭은: ", kor_rate)

# 미국 Daily 변동폭을 입력할 빈 리스트 형성
us_rate = []
# 다우존스 변동률 계산
def us(d):
    e = us_ma[d] - us_mi[d]
    f = (us_ma[d] - us_mi[d]) / us_mi[d] * 100
    return e,f

us_rate.append(us(1))
us_rate.append(us(2))
us_rate.append(us(3))
us_rate.append(us(4))
print("다우존스의 일일 변동폭은:", us_rate)

#### 3번 Guide Line ####
### 산술 평균은 더한 값의 평균, 기하평균은 곱의 평균이므로 변동성을 구하기 위해서는 기하평균을 사용
### 주간 변동성은 5일 단위이므로 제곱근 5를 곱해 산출한다.

# 변동률만 계산하기 위해 다시 리스트 생성 및 할당 작업
us_diff = []
kor_diff = []
def diff(g):
    h = (kor_ma[g] - kor_mi[g]) / kor_mi[g] * 100
    return h
kor_diff.append(diff(1))
kor_diff.append(diff(2))
kor_diff.append(diff(3))
kor_diff.append(diff(4))

def diff(i):
    j = (us_ma[i] - kor_mi[i]) / us_mi[i] * 100
    return j
us_diff.append(diff(1))
us_diff.append(diff(2))
us_diff.append(diff(3))
us_diff.append(diff(4))

# 3월 둘째 주 코스피와 다우 지수의 주간 변동성
# lambda라는 가상의 익명 함수를 만들어 변동률의 기하평균 계산
week_result_kor = list(map(lambda x: x**(1/5), kor_diff))
week_result_us = list(map(lambda y: y**(1/5), us_diff))

# 출력결과 코스피는 복소수형, 다우존스는 실수형 타입이었음.
print("코스피의 주간 변동성은: ", week_result_kor)
print("다우 지수의 주간 변동성은: ", week_result_us)

#### 4번 Guide Line ####
day = [2,3,4,5] # 2일부터 5일까지, 총 4일동안의 변동성을 계산하기 위해 일 리스트 형성
for k, l in zip(range(4), day): # 코스피, 다우지수의 리스트는 0부터 3까지, day 리스트를 for문의 변수로 취해 아래 식을 계산
    if abs(week_result_kor[k]) > week_result_us[k]: # 복소수와 실수의 연산이 불가하므로 복소수의 절대값을 구하는 함수 abs를 사용함.
        print(l,"일차는 코스피의 변동성이 높기 때문에 공매도 금지를 시행합니다.")
    else:
        print(l, "일차에는 코스피의 변동성이 낮기 때문에 공매도를 현행처럼 재개합니다.")

