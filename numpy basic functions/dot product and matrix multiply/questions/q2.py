import numpy as np
a = np.array([[2,4,5], [5,2,6]])
b = np.array([[1,5], [5,3], [9,0]])

# checking the shape of the array after multiplication 
arraymult = a @ b
print("Shape of the array is ", np.shape(arraymult))