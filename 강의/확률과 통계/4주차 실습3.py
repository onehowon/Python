import numpy as np
from scipy import linalg, sparse

A = np.matrix(np.random.random((2,2)))
b = np.random.random((2,2))
B = np.asmatrix(b)
C = np.mat(np.random.random((10,5)))
D = np.mat([[3,4], [5,6]])

print(linalg.eigvals(A)) # 행렬 A의 고윳값 확인

la, v = linalg.eig(A) # A의 고유 벡터
l1, l2 = la # 고윳값을 L1, L2로 받기
print(v[:,0]) # 첫 번째 고유 벡터
print(v[:,1]) # 두 번째 고유 벡터

C[C > 0.5] = 0
H = sparse.csr_matrix(C) # C를 희소행렬 형태로 변환
print(H.todense()) # H를 일반적인 행렬(dense matrix) 형태로 변환
print(sparse.isspmatrix_csr(H)) # 희소행렬 여부 확인