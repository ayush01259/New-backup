import numpy as np
mean = 100
std = 15
size = 500
data  = np.random.normal(mean, std, size)
print("Calculated mean =", np.mean(data))
print("Std deviation :", np.std(data))
