import numpy as np
a = np.array([0,1,2,3,4,5])
print(a.ndim) # ndim은 a의 차원 수를 알려준다

# 배열 a의 각 차원에 몇 개의 값이 있는지를 튜플로 반환한다. 값 6개를 갖는 1차원 배열은 다음처럼 표현된다.
print(a.shape)

# 배열 a의 값들의 타입을 알려주며, 아래 결과는 정수(integer)임을 의미.
print(a.dtype)

# 기본 인덱싱
a[[2,3,4]]
# 배열을 인덱싱으로 사용할 수 있다
a[np.array([2,3,4])]

print(a > 4)
print(a[a>4])