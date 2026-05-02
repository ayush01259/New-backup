import numpy as np

data = np.array([[2,0],[0,2],[3,1],[4,2]])


# to check the principal directions of the pca we have to find the covariance first with (np.cov(data.T)) then we have to find its eigenvector and eigenvalues like this


# Step 1: Covariance matrix
cov_matrix = np.cov(data.T)
print("Covariance matrix:\n", cov_matrix)



# Step 2: Eigen decomposition
values, vectors = np.linalg.eig(cov_matrix)

print("Eigenvalues:", np.round(values, 2))
print("Eigenvectors:\n", np.round(vectors, 3))

# Step 3: Verify Av = λv for first eigenpair
v1 = vectors[:,0]
l1 = values[0]
print("Check Av:", np.round(cov_matrix @ v1, 3))
print("Check λv:", np.round(l1 * v1, 3))
