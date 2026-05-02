# svd = singular value decomposition
# isme aap ek matrix ko 3 matrix me tod skte h 
# iska use signal processing, statics and machine learning me hota hai 

# A=UΣVT

# U → left singular vectors (orthogonal matrix)


# Σ → singular values (diagonal matrix, values = "importance" of each direction)

# VT → right singular vectors (orthogonal matrix ka transpose)

import numpy as np
A = np.array([[1,2],[3,4],[5,6]])

U, s , VT = np.linalg.svd(A)

print("Original matrix: \n", A)
print("\nU (left singular vectors):\n",U)
print("\nsingular values (sigma) :\n", s)
print("\nVT (right singular value) :\n", VT)


# if we want ki svd krne ke baad matrix ko wapas phle ke trh banana h to  kaise bnaynge
sigma = np.zeros((A.shape[0], A.shape[1]))
np.fill_diagonal(sigma, s)

A_reconstructed = U @ sigma @ VT
print(A_reconstructed)
