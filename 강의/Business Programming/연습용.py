import pandas as pd
from pandas import Series
import numpy as np


# 3월 9일부터 15일까지의 코스피 지수
kor_mi = Series([1,2,3,4,5])
kor_ma = Series([10,20,30,40,50])
us_mi = Series([3,4,5,6,7])
us_ma = Series([30,40,50,60,70])
### 네이버 증권 기준
# 한국 3월 9일부터 15일(13,14일은 휴장)까지의 코스피 지수
# 3/9 1947, 1990 / 1935,1968 / 1898,1968 / 1809, 1897 / 1681, 1809
# 미국 3월 9일부터 13일까지의 다우존스 지수
# 3/9 23,706, 24,922 / 23,690 ,25,020 / 23,328, 24,604 / 21,154, 22,837 / 21,285, 23,189 

# 변동폭 계산 최고점 - 최저점
diff_kor = kor_ma - kor_mi
diff_us = us_ma - us_mi

print(diff_kor)
print(diff_us)

rat = []

def rate(a):
    return kor_ma[a] - kor_mi[a]

rat.append(rate(1))
rat.append(rate(2))
rat.append(rate(3))
rat.append(rate(4))
print(rat)

print(rat * np.sqrt(5))