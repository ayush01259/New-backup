import numpy as np 
array = np.array([1,2,3,4,5,6,7,8,9,10])
masked = array>5
print("Number greater than 5 are", array[masked])

masked = array%2 ==0
print("Even numbers : ", array[masked])


arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("Selecitng with fancy indexing", arr[[1,2],:][:,[1,2]])
