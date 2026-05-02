import numpy as np 
A = np.random.randint(1,10, (3,3))
Q , R = np.linalg.qr(A)
print("A: \n", A)
print("Q: \n", np.round(Q, 2))
print("R: \n", np.round(R, 2))
print("Check A == Q@R ?  ", np.allclose(A, Q @ R))