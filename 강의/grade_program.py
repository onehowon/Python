import pandas as pd
import random
import math
import numpy as np

from pandas.core.algorithms import rank

#학번을 할당한다.
student_num = [1,2,3,4,5]
attend = [random.randint(0,10) for i in range(0, 5)]
mid = [random.randint(0,20) for j in range(0,5)]
final = [random.randint(0,20) for k in range(0,5)]
assignment = [random.randint(0,30) for p in range(0,5)]
frequent = [random.randint(0,20) for m in range(0,5)]

program = pd.DataFrame(list(zip(student_num, attend, mid, final, assignment, frequent)),
                       columns= ["학번","출석점수(10%)","중간고사(20%)","기말고사(20%)","과제점수(30%)","수시평가(20%)"]
                       )
program['총점(100)'] = program[["출석점수(10%)","중간고사(20%)","기말고사(20%)","과제점수(30%)","수시평가(20%)"]].sum(axis=1)
program['순위'] = program['총점(100)'].rank()
grade = [
    (program['총점(100)'] >= 70),
    (program['총점(100)'] >= 60),
    (program['총점(100)'] >= 50),
    (program['총점(100)'] >= 40),
    (program['총점(100)'] < 40),
]
grade_list = ['A','B','C','D','F']
program['학점'] = np.select(grade, grade_list)
print(program)

mid_mean = program['중간고사(20%)'].mean()
mid_max = program['중간고사(20%)'].max()
mid_median = program['중간고사(20%)'].median()
final_mean = program['기말고사(20%)'].mean()
final_max = program['기말고사(20%)'].max()
final_median = program['기말고사(20%)'].median()

exam_table = pd.DataFrame({'중간 평균':mid_mean,
                           '중간 최대':mid_max,
                           '중간 중앙값':mid_median,
                           '기말 평균':final_mean,
                           '기말 최대':final_max,
                           '기말 중앙값':final_median
                           }, index=['점수'])
print(exam_table)


