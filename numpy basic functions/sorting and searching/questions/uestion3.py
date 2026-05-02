import numpy as np 
array = np.random.randint(1,51, size=(3,3))
print(array)
print("Row wise sorting :", np.sort(array, axis=1))
print("Column wise sorting : ", np.sort(array, axis=0))