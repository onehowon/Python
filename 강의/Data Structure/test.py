from dataprep.eda import *
import pandas as pd

grade = pd.read_csv("grade.csv", encoding = 'EUC-KR')
plot(grade)