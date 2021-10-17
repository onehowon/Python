import sympy as sp
from scipy.optimize import fsolve
from scipy.integrate import quad
import numpy as np

##### 실습 1 #####
x = sp.Symbol('x')
print(sp.diff(3.0*x**2 + 1, x))

##### 실습 2 #####
line = lambda x: x+3
solution = fsolve(line, -2)
print(solution)

##### 실습 3 ####
# 적분할 함수 정의
func = lambda x: np.cos(np.exp(x))**2

# 0부터 3까지의 구간에 대해 함수 func를 적분
solution = quad(func, 0, 3)
print(solution)

#### 실습 4 ####
x = np.sort(np.random.randn(150) * 4 + 4).clip(0,5) # 0~5 사이의 랜덤한 값 생성
func = lambda x: np.sin(x) * np.cos(x**2) + 1
y = func(x)

fsolution = quad(func, 0, 5)
print(fsolution)

##### 실습 5 ####
x = sp.Symbol('x')
fx = sp.exp(2*x)*sp.sin(3*x)
dfx = sp.diff(fx,x)
ddfx = sp.diff(dfx,x)

k = sp.Symbol('k')
print(sp.factor(ddfx+k*dfx+13*fx)) # sp.factor = 인수분해