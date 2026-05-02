import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print("Where arr > 25:", np.where(arr>25)[0])
# yaha last me [0] islie dete h ki output list me aaye na ki tuple me 
# it return index on the basis of the condition
