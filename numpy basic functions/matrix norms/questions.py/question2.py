# Ek 4×4 matrix banao jisme kuch rows linearly dependent ho (jaise ek row dusre ki multiple ho) aur check karo rank kya aata hai.
import numpy as np
A = np.array([
    [1,2,3,4],
    [4,6,7,4],
    [2,4,6,8], # this is dependent row
    [3,0,2,1]
])
print(A)
print("Its rank is:", np.linalg.matrix_rank(A))
# its rank is 3 because it has one dependet row