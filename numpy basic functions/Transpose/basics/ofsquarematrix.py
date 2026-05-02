import numpy as np 
B = np.array([[1,2,0], [3,4,8]])
A = np.array([[1,2,3], [4,5,6]])
print("B : \n", B)
print("B transpose : \n", B.T)
print("B transpose transpose : \n", B.T.T)

# (CD)T  = DT CT
# product ka transpose lena h jisme order reverse ho jata h 
C = np.array([[1,2], [3,4]])
D = np.array([[5,6], [7,8]])

lhs = (C @ D).T

rhs = D.T @ C.T

print("LHS:\n", lhs)
print("RHS: \n", rhs)
print("Are they equal ?", np.array_equal(lhs,rhs))


# (A + B)T = AT + BT
# lhs = (A + B ).T
left_hs = (A+B).T

#rhs = A.T + B.T

right_hs = A.T + B.T

print("LHS = ", left_hs)
print("RHS =", right_hs)
print("Are they equal =", np.array_equal(left_hs,right_hs))
