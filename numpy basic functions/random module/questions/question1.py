import numpy as np
array = np.random.randint(1, 101, size=(5,5))
print("The 5 by 5 array is :\n", array)

print("max :", np.max(array))
print("Min :", np.min(array))
print("Mean : ", np.mean(array))
print("Std deviation:", np.std(array))
