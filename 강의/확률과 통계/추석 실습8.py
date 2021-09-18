import numpy as np

x = [0.0, 1, 2, 3, 4]
y = np.array(x) # 0.0으로 인해 다른 1,2,3,4도 모두 실수혀으로 변경되어 배열을 생성
y = np.array([[0.0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]) # 2차원 배열 생성
print(np.shape(y)) # 행과 열을 확인

y = np.array([[[1,2],[3,4]], [[5,6], [7,8]]]) # 3차원 배열 생성
print(np.shape(y)) # 2개의 2차원 배열, 각 2차원 배열은 2행 2열임을 순서대로 의미한다.

a = np.array([[1,2],[3,4], [5,6]], float) 
for x in a:
    print(x)