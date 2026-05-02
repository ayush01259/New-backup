import numpy as np
arr2d = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

print(arr2d[0,0])
# iska mtlb ho gya 0th row and 0th column mtlb dono ke 1st elemnt so the output will be [1]

print(arr2d[1,2])
#iska mtlb 1st row aur 2nd column element wise 2nd row aur last col so the output will be [6]

print(arr2d[-1,2])
# iska mltb ho jygea last row aur uska 2nd col meaning the output will be 9

print(arr2d[-1,-1])
#last row and the last col means the output will be 9 too

