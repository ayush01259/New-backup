# norm question
# 2x2 ka matrix ka frobenius norm nikalna hai ( sab element ka square ka sum ka root)

import numpy as np
A = np.array([[2,4],[3,5]])
print(A)
forbenius = np.sqrt(np.sum(A**2))
print("Forbenius norm ( manually ) :", forbenius)

forbenius_np = np.linalg.norm(A, 'fro')
print("Forbenius norm (numpy ): ", forbenius_np)