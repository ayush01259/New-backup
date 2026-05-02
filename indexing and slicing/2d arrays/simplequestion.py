import numpy as np
arr = np.array([[1, 2, 3, 4], [5,6,7,8], [9,10,11,12], [13, 14,15,16]])
print(arr)

# to print the last 2 rows
print("The last two rows of the array is : ",arr[2: , :])

# printing the middle two columns 
print("The middle two columns are :\n", arr[:, 1:3])


# printing the 2x2 bottom right block 
print("The 2x2 bottom right block are :\n", arr[2:4, 2:4])