import numpy as np
array = np.array([1,2,3,4,5])

# 1st way : Manual method
squared = []
for i in array:
    squared.append(int(i**2))

print("Squared manually : ", squared)

# 2nd way : vectorization  method (1st method)
squared_Vec = array ** 2
print("1st vector method", squared_Vec)

#3rd way : vectorization method (2nd method)
squared_vec = np.square(array)
print("2nd vector method: ", squared_vec)