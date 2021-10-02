import pandas as pd
import numpy as np 

### 네이버 증권 기준
# 한국 3월 9일부터 13일까지의 코스피 지수
# 3/9 1989.50, 1946.90 / 1968.17,1934.72 / 1967.70,1898.27 / 1897.23, 1808.56 / 1809.31, 1680.60

# 미국 3월 9일부터 13일까지의 다우존스 지수
# 3/9 24922.36, 23706.07 / 25020.99 ,23690.34 / 24604.63, 23328.32 / 22837.95 21154.46 / 23189.76, 21285.37

#### 1번 Guide Line ####
# 3월 9일부터 15일까지의 코스피 지수
kor_ma = list(map(float,input("3월 9일부터 13일까지의 한국 코스피 지수의 최고점을 5개 입력하세요.>").split()))
kor_mi = list(map(float,input("3월 9일부터 13일까지의 한국 코스피 지수의 최저점을 5개 입력하세요.>").split()))
us_ma = list(map(float,input("3월 9일부터 13일까지의 미국 다우존스 지수의 최고점을 5개 입력하세요.>").split()))
us_mi = list(map(float,input("3월 9일부터 13일까지의 미국 다우존스 지수의 최저점을 5개 입력하세요.>").split()))

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
kor_rate.append(kor(0))
kor_rate.append(kor(1))
kor_rate.append(kor(2))
kor_rate.append(kor(3))
kor_rate.append(kor(4))
print("코스피의 일일 변동폭과 변동률은: ", kor_rate)

# 미국 Daily 변동폭을 입력할 빈 리스트 형성
us_rate = []
# 다우존스 변동률 계산
def us(d):
    e = us_ma[d] - us_mi[d]
    f = (us_ma[d] - us_mi[d]) / us_mi[d] * 100
    return e,f

us_rate.append(us(0))
us_rate.append(us(1))
us_rate.append(us(2))
us_rate.append(us(3))
us_rate.append(us(4))
print("다우존스의 일일 변동폭과 변동률은:", us_rate)

#### 3번 Guide Line ####
### 산술 평균은 더한 값의 평균, 기하평균은 곱의 평균이므로 변동성을 구하기 위해서는 기하평균을 사용
### 주간 변동성은 5일 단위이므로 제곱근 5를 곱해 산출한다.

# 변동률만 계산하기 위해 다시 리스트 생성 및 할당 작업
us_diff = []
kor_diff = []
def diff(g):
    h = (kor_ma[g] - kor_mi[g]) / kor_mi[g] * 100
    return h
kor_diff.append(diff(0))
kor_diff.append(diff(1))
kor_diff.append(diff(2))
kor_diff.append(diff(3))
kor_diff.append(diff(4))

def diff(i):
    j = (us_ma[i] - us_mi[i]) / us_mi[i] * 100
    return j
us_diff.append(diff(0))
us_diff.append(diff(1))
us_diff.append(diff(2))
us_diff.append(diff(3))
us_diff.append(diff(4))

# 3월 둘째 주 코스피와 다우 지수의 주간 변동성
# 변동률의 기하평균 계산
week_result_kor = (kor_diff[0]*kor_diff[1]*kor_diff[2]*kor_diff[3]*kor_diff[4]) ** (1/5)
week_result_us = (us_diff[0]*us_diff[1]*us_diff[2]*us_diff[3]*us_diff[4]) ** (1/5)

print("코스피의 주간 변동성은: ", week_result_kor)
print("다우 지수의 주간 변동성은: ", week_result_us)

#### 4번 Guide Line ####
if week_result_kor > week_result_us:
    print("코스피의 변동성이 다우존스보다 높기 때문에 공매도 금지를 시행합니다")
else:
    print("코스피의 변동성이 낮기 때문에 공매도를 현행처럼 재개합니다.")