# import numpy as np 
# A = np.random.randint(1,53, size=(4,4))
# U, s, VT = np.linalg.svd(A)
# print("U : \n", U)
# print("s : \n", s)
# print("VT : \n", VT)
# print(A)
# # reconstruction 
# sigma = np.zeros((A.shape[0], A.shape[1]))
# np.fill_diagonal(sigma, s)

# A_reconstructed = U @ sigma @ VT
# print("Reconstructed array : ", np.round(A_reconstructed,2))

# print("Are they equal :", np.allclose(A, A_reconstructed))




# we can do the same like this too





import numpy as np 

A = np.random.randint(1,53, size=(4,4))
U, s, VT = np.linalg.svd(A)
print("Original A:\n", A)

# Sigma banana
sigma = np.zeros((A.shape[0], A.shape[1]))
sigma[:len(s), :len(s)] = np.diag(s)   # singular values diagonal me

# Reconstruction
A_reconstructed = U @ sigma @ VT
print("Reconstructed A:\n", np.round(A_reconstructed, 2))

# Verify
print("Are they equal:", np.allclose(A, A_reconstructed))
