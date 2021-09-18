from pandas import Series, DataFrame
import numpy as np

s = Series([0.1, 1.2, 2.3, 3.4, 4.5], index = ['a','b','c','d','e'])
print(s['a'])
print(s[0])
print([['a','c']])
print(s[[0,2]])
print(s[s>2])

s1 = Series({'a': 0.1, 'b' : 0.2, 'c' : 2.3})
s2 = Series({'a':1.0, 'b' : 2.0, 'c' : 3.0})
print(s1 + s2)

s1 = Series(np.arange(10.0, 20.0))
print(s1.describe())

summ = s1.describe()
print(summ['mean'])

s1 = Series(np.arange(1.0,6), index = ['a','a','b','c','d'])
print(s1.drop('a'))