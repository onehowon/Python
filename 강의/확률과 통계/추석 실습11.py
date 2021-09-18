from pandas import Series, DataFrame
import numpy as np

raw_data = {'col0':[1,2,3,4],
'col1':[10,20,30,40],
'col2':[100,200,300,400]}

data = DataFrame(raw_data)

print(data)

a = np.array([[1.0,2],[3,4]])
df = DataFrame(a, columns = ['dogs','cats'], index=['Alice','Bob'])
print(df)