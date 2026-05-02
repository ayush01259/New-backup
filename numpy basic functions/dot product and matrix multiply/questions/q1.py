import numpy as np
a = np.array([2,3,4])
b = np.array([1,0,1])

# dot product by manual way
dot_manual = a[0]*b[0] + a[1] * b[1] + a[2]* b[2]

# by numpy way
dot_1 = np.dot(a, b)
dot_2 = a @ b

print("Manually doing :", dot_manual)
print("1st way of numpy:", dot_1)
print("2nd way of numpy", dot_2)