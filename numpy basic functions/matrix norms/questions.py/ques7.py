# svd ( singular value decomposition )
import numpy as np 
A = np.random.randint(1,53, size=(3,2))
print(A)
U, s, VT = np.linalg.svd(A)

print("U : \n", U)
print("s : \n", s)
print("VT: \n", VT)