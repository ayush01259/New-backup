import numpy as np
S = np.array([[2,1],[1,2]])
values, vector = np.linalg.eigh(S)
print("Eigen value:",values)
print("Eigen vecotr:", vector)
#to verify vectors are orthogonal (dot proudct ~ 0)
# here we have to find the dot product of the vectors to check its orthogonality 
v1 = vector[:,0]
v2 = vector[:,1]
dot_product = np.dot(v1, v2)
print("Dot product (shoud le ~0)", round(dot_product,4))