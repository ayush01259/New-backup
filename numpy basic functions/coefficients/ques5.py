import numpy as np
p = np.array([[1,2,1], [2,1,1], [3,2,4]])
c = np.array([40,50,120])
print("For pcf", np.linalg.solve(p,c))