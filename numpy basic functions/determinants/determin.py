#Determinants is a scalar value come from a square matrix only
import numpy as np 
A = np.array([[2,3], [4,9]])
det_A = np.linalg.det(A)
print("Matrix A:\n", A)
print("Determinant of A : ", det_A)

# for higer dimensions
B = np.array([[1,2,3], [0, 3,2],[2,4,2]])
print("Determinant of B :\n", np.linalg.det(B))
