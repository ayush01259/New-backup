import numpy as np
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])

print("Fancy indexed rows and columns :", arr[[0,2], [1,2]])
# it select the element form 0th and 2nd row and the oth and 2nd column 



# using it with conditions 
mask = arr>2
print("Filterd using fancy indexing : ", arr[mask])
print(mask)