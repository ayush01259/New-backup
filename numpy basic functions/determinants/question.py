import numpy as np
S = np.array([[1,2], [4,9]])
det_s = np.linalg.det(S)
print("Manually determinat :\n", det_s)
print("By numpy: \n", np.linalg.det(S))


# true way to do manually 
manual = S[0,0]*S[1,1] - S[0,1]*S[1,0]
print(manual)