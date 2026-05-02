#question 1 : create a default array and print it and then check its flag and then make the array as order = "F" and then check flag

import numpy as np
arr = np.array([[1,2,3],
                [4,5,6]])
arr = np.array([[1, 2, 3],
              [4, 5, 6]], order='F')
print(arr)
print(arr.flags)

