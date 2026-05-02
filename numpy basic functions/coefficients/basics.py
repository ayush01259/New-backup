# solving linear equations with np.linalg.solve
import numpy as np
# ax = b on 2x2 matrix
A = np.array([[1,2], [3,9]])
b = np.array([2,1])
x = np.linalg.solve(A, b)
print(x)

# ax = b on 3 by 3 matrix
c = np.array([[1,1,1], [0,2,5], [2,5,-1]])
d = np.array([6,-4,27])
print(np.linalg.solve(c,d))


# we can also use np.linalg.inv(A) @ b here but it would give slower and less stable answer
print(np.linalg.inv(A)@b)

# we can use np.linalg.matrix_rank(A) to check the system has unique solution (rank = n) 
print(np.linalg.matrix_rank(A))