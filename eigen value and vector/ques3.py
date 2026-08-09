import numpy as np 
D = np.array([[5, 0,0], [0, 7, 0], [0, 0,9]])
value, vector = np.linalg.eig(D)
print("Eigen value:", value)
print("Eigen vector:", vector)