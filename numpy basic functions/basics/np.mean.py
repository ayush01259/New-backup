import numpy as np 
arr = np.array([10,20,30,40,50])
print("the mean of the array is: ", np.mean(arr))


# for 2d array
array = np.array([[1,2,3], [4,5,6]])
print("The mean for the row of the 2d array is : ", np.mean(array, axis=1))
print("The mean of the column of the array is: ", np.mean(array, axis=0))