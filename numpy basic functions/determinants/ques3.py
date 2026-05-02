import numpy as np
A = np.random.randint(1,10, size=(3,3))

while np.linalg.det(A) == 0:
    A = np.random.randint(1,10, size=(3,3))


print("Matrix A: \n", A)

# (A−1)T=(AT)−1 yeh krna h verify

lhs = np.transpose(np.linalg.inv(A))
rhs = np.linalg.inv(np.transpose(A))

print("\n(A^-1).T:\n", lhs)
print("\n(A.T)^-1:\n", rhs)

print("Are they equal?", np.allclose(lhs,rhs))

# its only true whn A is invertible means A is not equals to zero
