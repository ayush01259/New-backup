import numpy as np

A = np.array([[1,2,3],
              [4,5,6]])

print("Original:\n", A)
print("Transpose using .T:\n", A.T)
print("Transpose using np.transpose:\n", np.transpose(A))
