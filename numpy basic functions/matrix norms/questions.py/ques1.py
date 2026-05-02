# rank question1 
# a 3 by 3 matrix and find its rank
import numpy as np
A = np.random.randint(1,54, size=(3,3))
print(A)
print("its rank: ", np.linalg.matrix_rank(A))
# this is how ranks works
# rank in inverserly proportional to independent rows
# if rank = 1 then here independent rows will be 2