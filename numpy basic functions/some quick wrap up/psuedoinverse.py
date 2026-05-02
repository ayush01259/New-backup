import numpy as np

A = np.array([[1, 2], [3, 6]])  # singular matrix (det=0)
print("Normal inverse (will error if tried)")
print("Pseudo-inverse:\n", np.linalg.pinv(A))
