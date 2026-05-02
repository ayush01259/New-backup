# yeh array ko ascending order me sort krta hai

import numpy as np
arr = np.array([12, 4, 56, 1, 34])
print("Original:", arr)
print("Sorted = ", np.sort(arr))


# in 2d array
array = np.random.randint(1,89, size=(3,3))
print("Original array  :", array)
print("Row wise sort :\n", np.sort(array, axis=1))
print("Column wise sorting :\n", np.sort(array, axis=0))
