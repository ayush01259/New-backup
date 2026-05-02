# a.b = a1b1 + a2b2 + .... + anbn krna h 
import numpy as np 
a = np.array([1,2,3])
b = np.array([4,5,6])

# manual way to do this 
dot_manual = a[0]*b[0] + a[1]*b[1] + a[2]*b[2] 

# numpy ways
# 1st way
dot_numpy = np.dot(a,b)

# 2nd way
dot_operator = a @ b

print("Manual way:", dot_manual)
print("Np dot way:", dot_numpy)
print("@ operator method:", dot_operator) 