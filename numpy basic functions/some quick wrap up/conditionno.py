import numpy as np 
A = np.array([[1,2], [2,4.0001]])
print("Condition number: " , np.linalg.cond(A))
# numerical stability check krta h jisme high condition number hone pr system unstable ho jata h 
# agar conditon >> 1 h to matrix ill conditioned h numerical error  ho skta h isme

