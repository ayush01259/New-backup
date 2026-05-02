import numpy as np
A = np.random.randint(1,38, size=(4,4))
print("Original array :\n", A)

lhs = A
rhs = A.T
print("Symmetric or not:", np.array_equal(lhs, rhs))
