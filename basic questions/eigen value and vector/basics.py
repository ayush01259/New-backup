# eigenvectors are the vectors in which their directions didnt change by transforming (rotating , streching or squashing ) matrix only their length are changed
# eigen values are values in which the length of the matrices are changed

import numpy as np
A = np.array([[1,2], [3,4]])

eigenvalue, eigenvector = np.linalg.eig(A)

# tip: for a symmetric matrix we use np.linalg.eigh()
print("Eigenvalue of the matrix A is :\n", np.round(eigenvalue, 2)) 
# here np.round(, 2) means it allows 2 decimal 
print("Eigenvector of the matrix A is :\n", np.round(eigenvector,2))
# here it also denotes 2 decimals

# to verify we will do A⋅v=λv
V1 = eigenvector[:,0]
L1 = eigenvalue[0]

print("AV = ", A @ V1)
print("λv = ", L1 * V1)