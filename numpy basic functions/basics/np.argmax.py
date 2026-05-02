# isse array ki index ki maximum valuue nikal skte hai
import numpy as np 
arr = np.array([10,20,30,40,50])
print("Index of maximum value : ", np.argmax(arr))



# for 2d array
array = np.array([[1,2,3], [4,5,6]])
print(np.argmax(array))# for the whole 2d array, yha 2*3 ka array h toh 5th index me 6 biggest h toh wo de rha 
print(np.argmax(array, axis=1))# for entrie rows, sare rows ka max value ka index milega 
print(np.argmax(array, axis=0)) # for entire columns, sare columns ke max value ka index milega