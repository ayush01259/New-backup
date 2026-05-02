import numpy as np
A = np.random.randint(1,10, size=(3,3))
print(A)
value, vectors = np.linalg.eig(A)
print("Eigenvector:",vectors)
print("Eigenvalue:", value)


# verifying AV = Lemda.v
v = vectors[:,0]
l = value[0]
print("AV:", np.round(A @ v,2))
print("LV:", np.round(l*v,2))