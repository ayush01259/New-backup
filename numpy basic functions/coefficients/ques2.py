import numpy as np 
A = np.array([[3,2,1,],[2,-2,4],[-1,0.5,-1]])
B = np.array([1,-2,0])
print("Solution:", np.linalg.solve(A,B))