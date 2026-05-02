# it is used for standard deviation 
# data analysis me iska bht use h

import numpy as np 
arr = np.array([10,20,30,40,50])
print("standard deviation :", np.std(arr))



# for 2d array
array = np.array([[1,2,3], [4,5,6]])
print(np.std(array, axis=1))
print(np.std(array, axis=0))