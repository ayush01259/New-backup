import numpy as np
A = np.random.randint(1, 24, size=(2,2))
B = np.random.randint(1,27, size=(2,2))


lhs = (A @ B).T
rhs = B.T @ A.T
print(lhs)
print(rhs)

print("Are those two equal or not:", np.array_equal(lhs, rhs))