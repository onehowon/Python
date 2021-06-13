import pandas as pd
import random
import math
import numpy as np

from pandas.core.algorithms import rank

# 학번을 할당한다.
student_num = [1,2,3,4,5]
# 출석 점수 할당(0부터 10까지의 임의의 난수)
attend = [random.randint(0,10) for i in range(0, 5)]
# 중간, 기말, 과제, 상시평가 또한 숫자 범위를 정해 임의의 난수를 할당하게함
mid = [random.randint(0,20) for j in range(0,5)]
final = [random.randint(0,20) for k in range(0,5)]
assignment = [random.randint(0,30) for p in range(0,5)]
frequent = [random.randint(0,20) for m in range(0,5)]

# pandas 모듈을 이용해 난수 단위로 묶인 숫자형 리스트들을 데이터프레임으로 병합함
# 컬럼 이름은 과제 파일에 나온 것과 같이 설정
program = pd.DataFrame(list(zip(student_num, attend, mid, final, assignment, frequent)),
                       columns= ["학번","출석점수(10%)","중간고사(20%)","기말고사(20%)","과제점수(30%)","수시평가(20%)"]
                       )

# 각 컬럼들의 합을 총점이라는 새로운 컬럼을 만들어 합계를 할당
# sum(axis=1)은 합의 연산이 행 안에서 수행되도록 정해주는 조건이다.
program['총점(100)'] = program[["출석점수(10%)","중간고사(20%)","기말고사(20%)","과제점수(30%)","수시평가(20%)"]].sum(axis=1)

# rank 함수를 사용해 총점을 기준으로 순위를 나열하도록 함(rank 함수 특성상 소수점 형태로 출력됨)
program['순위'] = program['총점(100)'].rank()

# 학점을 부여하는 기준표 리스트 작성
grade = [
    (program['총점(100)'] >= 70),
    (program['총점(100)'] >= 60),
    (program['총점(100)'] >= 50),
    (program['총점(100)'] >= 40),
    (program['총점(100)'] < 40),
]
grade_list = ['A','B','C','D','F']

# 조건에 맞게 학점 할당
program['학점'] = np.select(grade, grade_list)
print(program)

# 중간고사와 기말고사의 평균, 최대, 최소값을 할당
mid_mean = program['중간고사(20%)'].mean()
mid_max = program['중간고사(20%)'].max()
mid_median = program['중간고사(20%)'].median()
final_mean = program['기말고사(20%)'].mean()
final_max = program['기말고사(20%)'].max()
final_median = program['기말고사(20%)'].median()

# 데이터프레임으로 만들어줌
exam_table = pd.DataFrame({'중간 평균':mid_mean,
                           '중간 최대':mid_max,
                           '중간 중앙값':mid_median,
                           '기말 평균':final_mean,
                           '기말 최대':final_max,
                           '기말 중앙값':final_median
                           }, index=['점수'])
print(exam_table)


