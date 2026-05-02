import numpy as np 
a = np.array([2,4,6,8,10])
b= np.array([1,2,3,4,5])

print("elements of b in a", np.in1d(b, a))