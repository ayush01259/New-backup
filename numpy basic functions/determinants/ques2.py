import numpy as np 
A = np.random.randint(1,10, size=(3,3))
print(A)
deter = round(np.linalg.det(A))
# using round instead of int bcz int is only safe for small integer matrices
print("determinant of a random 3 by 3 array is: ", deter)

