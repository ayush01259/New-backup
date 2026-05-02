# so the question is to do f(x) = x*2 + 2x in both manual and vectorized way 

import numpy as np
arr = np.array([1,2,3,4,5])

#manually 
arr_square = []
for x in arr:
    arr_square.append(int(x**2 + 2*x))
print("Manual way ", arr_square)

arr_sq = [int(z**2+ 2*z) for z in arr]
print("array squared again with different way manually : ", arr_sq)

# now the time for vecotrised way
arr_sq_vec = arr**2 + 2*arr
print("The same result in vectorized way : ", arr_sq_vec)
datatype = arr_sq_vec.dtype
print(datatype)
datain32 = arr_sq_vec.astype(np.int32)
