##
#   출석인정과제 : 리히터 규모를 받아서 피해정도를 출력한다.
#   202021524_성원호
#
Scale = float(input("리히터 규모를 입력하시오: "))
if Scale < 2.0:
    print("지진계에 의해서만 탐지 가능합니다.")
elif 2.0 <= Scale <= 3.9:
    print("물건들이 흔들리거나 떨어집니다.")
elif 4.0 <= Scale <= 6.9:
    print("빈약한 건물에 큰 피해가 있습니다.")
elif 7.0 <= Scale <= 7.9:
    print("지표면에 균열이 발생합니다.")
else:
    print("대부분의 구조물이 파괴됩니다.")

##
#   이 프로그램은 산수 문제를 출제한다.
#

import random

x = random.randint(1,100)
y = random.randint(1,100)

answer = int(input(f"{x} + {y} = "))

# 부울 변수에 결과를 저장하고 출력한다.
flag = (answer == (x+y))
print(flag)

##
#   조건 연산자
#
price = int(input("상품의 가격:"))
if price > 20000:
    shipping_cost = 0
else:
    shipping_cost = 3000
# 배송비 출력
print("배송비 =", shipping_cost)

##최대, 최소, 절대값 산
shipping_cost = ( 0 if price >= 20000 else 3000)
absolute_value = (x if x > 0 else -x)
max_value = (x if x > y else y)
min_value = (x if x < y else y)

## 실습 2
# 홀수/짝수를 검사한다.
#
number = int(input("정수를 입력하시오: "))
if number % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

## 실습 3
# 세일 가격 계산
#
price_tag = int(input("정가를 입력하시오: "))
if price_tag >= 100:
    dis_rate = 0.85
    print("10층에서 사은품을 받아가세요.")
else:
    dis_rate = 0.90
dis_price = dis_rate * price
print("할인된 상품의 가격=", dis_price)

## 실습 4
# 배송비 계산 프로그램
#
country = input("배송지(현재는 korea와 us만 가능):")
price_product = int(input("상품의 가격: "))

# 배송비를 결정한다.
if country == "korea":
    if price_product >= 20000:
        shipping_cost = 0
    else:
        shipping_cost = 3000
else:
    if price_product >= 100000:
        shipping_cost = 0
    else:
        shipping_cost = 8000
#배송비를 출력한다.
print("배송비 =", shipping_cost)

