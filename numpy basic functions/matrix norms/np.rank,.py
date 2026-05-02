import numpy as np 
a = np.array([[1,2,3],[2,4,6],[3,6,9]])
print("Rank : ", np.linalg.matrix_rank(a))
# rank is no of independent rows or columns
# it is useful in ML / DL as full rank matrix = invertible
