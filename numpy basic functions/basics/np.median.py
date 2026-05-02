import numpy as np 
arr = np.array([10,20,30,40,50])
print("Median:", np.median(arr)) 



# for 2d array
array = np.array([[1,2,3], [4,5,6]])
print("Median:", np.median(array, axis=1)) 
print("Median:", np.median(array, axis=0)) 