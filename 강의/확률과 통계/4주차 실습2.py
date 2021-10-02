import numpy as np
from scipy import linalg, sparse

A = np.matrix(np.random.random((2,2)))
b = np.random.random((2,2))
B = np.asmatrix(b)
C = np.mat(np.random.random((10,5)))
D = np.mat([[3,4], [5,6]])

print(A)
print(B)
print(C)
print(D)

print("A의 역행렬은", A.I)
print("A의 행렬식은", linalg.det(A))

print("A의 전치행렬은", A.T)
print(np.add(A,D))
print(np.subtract(A,D))
print(np.divide(A,D))

print("D와 B의 행렬곱은", D@B)
print("D와 B의 행렬곱을 dot으로 계산시에", np.dot(D,B))
print("원소끼리의 단순 곱셈은", np.multiply(D,B))
print("벡터의 외적 값은", np.cross(D,B))

G = np.mat(np.identity(2))
print("2*2 항등행렬은", G)

