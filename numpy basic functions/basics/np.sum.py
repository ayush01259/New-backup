import numpy as np 
arr = np.array([10,20,30,40,50])

print("Total sum of the 1d array is: ", np.sum(arr))


# for 2d array
array = np.array([[1,2,3], [4,5,6]])
print("Row wise sum of the array :", np.sum(array, axis=1))

print("Column wise sum =", np.sum(array, axis=0))