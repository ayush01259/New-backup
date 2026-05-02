#variance nikalne ke lie iska use hota hai
import numpy as np 
arr = np.array([10,20,30,40,50])
print("Variance", np.var(arr))



# for 2d array
array = np.array([[1,2,3], [4,5,6]])
print(np.var(array, axis=1))
print(np.var(array, axis=0))
