import numpy as np
arr = np.array([1,2,2,3,4,4,5,6,6])
a = np.array([1,2,3,4])
b = np.array(([3,4,5,6]))
print("Union:", np.union1d(a, b))
# it returns the array with the unique elements in both of the elements
