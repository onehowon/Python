import pandas as pd

# 3월 9일부터 15일까지의 코스피 지수
kor_mi = list(map(int,input("3월 9일부터 13일까지의 한국 코스피 지수의 최고점을 5개 입력하세요.>").split()))
kor_ma = list(map(int,input("3월 9일부터 13일까지의 한국 코스피 지수의 최저점을 5개 입력하세요.>").split()))
us_mi = list(map(int,input("3월 9일부터 13일까지의 미국 코스피 지수의 최고점을 5개 입력하세요.>").split()))
us_ma = list(map(int,input("3월 9일부터 13일까지의 미국 코스피 지수의 최저점을 5개 입력하세요.>").split()))
### 네이버 증권 기준
# 한국 3월 9일부터 15일(13,14일은 휴장)까지의 코스피 지수
# 3/9 1947, 1990 / 1935,1968 / 1898,1968 / 1809, 1897 / 1681, 1809
print(kor_mi)
print(kor_ma)
# 미국 3월 9일부터 13일까지의 다우존스 지수
# 3/9 23,706, 24,922 / 23,690 ,25,020 / 23,328, 24,604 / 21,154, 22,837 / 21,285, 23,189 
print(us_mi)
print(us_ma)

date = ["3/9", "3/10", "3/11", "3/12", "3/13"]

stock_df = pd.DataFrame(data = [[kor_ma, kor_mi, us_ma, us_mi]], columns=['코스피 최고', '코스피 최저', '다우존스 최고', '다우존스 최저'])
print(stock_df)