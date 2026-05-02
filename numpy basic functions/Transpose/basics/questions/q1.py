import numpy as np
A = np.array([[29,10], [24,53],[30,25]])
# printing the original matrix
print("Original : ", A)
# 1st way to transpose this
print("Using .T method", A.T)
# 2nd way to tranpose this 
print("Using np method", np.transpose(A))