# row of first multiply column of second
import numpy as np
A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])
 
 # matrix multiplication
C1 = np.dot(A, B)
C2 = A @ B
print("Matrix multiplication:", C1)
