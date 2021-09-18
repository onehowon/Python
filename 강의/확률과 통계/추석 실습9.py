import numpy as np

arr = np.arange(10, dtype = float).reshape((2,5))
print(arr[0]) # 1행
print(arr[0,3]) # 1행 3열
print(arr[0][3]) # 1행 3열
print(arr[0, :])
print(arr[:, 0])