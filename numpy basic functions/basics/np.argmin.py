import numpy as np 
arr = np.array([10,20,30,40,50])
print("Min value of the index:", np.argmin(arr))



# for 2d array
array = np.array([[1,2,3], [4,5,6]])
print(np.argmin(array))# pure array me jo index me minimum value hoga wo dega
print(np.argmin(array, axis =1))# sare rows se ek ek min value index dega
print(np.argmin(array, axis=0))# sare columns me se ek ek index dega