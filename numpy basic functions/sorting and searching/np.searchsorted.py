import numpy as np
arr = np.array([10,20,30,40,50])
print("Insert position for 25: ", np.searchsorted(arr, 15))
print("insert positon for 40:", np.searchsorted(arr, 40))