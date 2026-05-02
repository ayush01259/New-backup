import numpy as np 
A = np.array([[1,1], [2,-1]])
B = np.array([10,3])
print("Solution:", np.linalg.solve(A,B))