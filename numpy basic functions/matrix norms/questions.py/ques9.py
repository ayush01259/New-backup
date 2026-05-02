import numpy as np

# --- Step 1: Make a 6x6 "image-like" matrix (grayscale 0-255)
np.random.seed(0)  # reproducible
A = np.random.randint(0, 256, size=(6, 6))
print("Original 6x6 matrix (image-like):\n", A, "\n")

# --- Step 2: Compute SVD
U, s, VT = np.linalg.svd(A, full_matrices=False)  # s is a 1D array of singular values
print("Singular values (sorted desc):\n", np.round(s, 4), "\n")

# --- Step 3: Energy (variance) explained by singular values
singular_vals_squared = s**2
total_energy = singular_vals_squared.sum()
cumulative_energy = np.cumsum(singular_vals_squared) / total_energy * 100  # percent

print("Singular values squared (proportional to energy):\n", np.round(singular_vals_squared, 4))
print("\nCumulative energy explained (in %):\n", np.round(cumulative_energy, 2), "\n")

# Helpful summary: how many singular values to keep for 90% energy
k_90 = np.searchsorted(cumulative_energy, 90) + 1  # +1 because index->count
print(f"Number of singular values to capture >=90% energy: {k_90}\n")

# --- Step 4: Low-rank approximation using top-k (example: top-2)
k = 2
Sigma_k = np.diag(s[:k])
U_k = U[:, :k]
VT_k = VT[:k, :]

A_approx_k = (U_k @ Sigma_k) @ VT_k
print(f"Low-rank approximation using top-{k} singular values:\n", np.round(A_approx_k, 2), "\n")

# --- Step 5: Error metric (Frobenius norm)
error = np.linalg.norm(A - A_approx_k, ord='fro')
rel_error = error / np.linalg.norm(A, ord='fro')
print(f"Frobenius norm of (A - A_approx_{k}): {error:.4f}")
print(f"Relative error: {rel_error:.4f} (fraction of original matrix norm)\n")
