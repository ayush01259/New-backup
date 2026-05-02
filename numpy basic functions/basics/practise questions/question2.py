import numpy as np 
# array = np.arange(1,10).reshape(3,3)
array = np.random.randint(1,51, size=(3,3))
print(array)
print("The row wise sumo the array is :",np.sum(array, axis=1))
print("The column wise sum of the array is :", np.sum(array, axis=0))
print("The minimum of the array is :", np.min(array), "and the maximum of the array is :", np.max(array))
