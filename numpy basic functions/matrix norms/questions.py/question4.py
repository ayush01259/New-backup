# trace (A  +  B) = trace(A) + trace(B) nikalna hai 

import numpy as np 
A = np.random.randint(1,42, size=(3,3))
B = np.random.randint(1,42, size=(3,3))
trace_rhs = np.linalg.trace(A) + np.linalg.trace(B)
trace_lhs = np.linalg.trace(A + B)
print("Trace(A+B):", trace_lhs)
print("Tace(A) + Trace(B) :", trace_rhs)
print("Are they equal:",trace_lhs == trace_rhs)