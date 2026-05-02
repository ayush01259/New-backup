import numpy as np 
A = np.array([[4,2],[1,3]])
values, vector = np.linalg.eig(A)
print("Eigenvalue  :", values)
print("Eigenvectors  :", vector)

# verifying Av = lemda.v
v1 = vector[:,0]
L1 = values[0]

print("AV:", A @ v1)
print("Lemda.v:", L1 * v1)