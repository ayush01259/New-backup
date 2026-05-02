import numpy as np
A = np.array([[1,1,1], [2,5,1], [2,3,8]])
B = np.array([6,-4,27])
print("Solution:", np.linalg.solve(A,B))