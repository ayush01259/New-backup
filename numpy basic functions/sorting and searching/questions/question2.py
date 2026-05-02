import numpy as np 
array = np.array([5, 10, 15, 20, 25,30, 35])
print("elements > 20 indexes : ", np.where(array>20)[0])
print("Insert position of 22 and 30 are", np.searchsorted(array,22), "and", np.searchsorted(array, 30))