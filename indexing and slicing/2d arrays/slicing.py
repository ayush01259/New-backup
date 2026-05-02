import numpy as np
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# selecting row with :
print(arr2d[1, :])
# iska mltb 1st row ke sare elements aur koi v colunns nhi 
# output ho jyega [4,5,6]


# selecting columns with:
print(arr2d[:, 1])
#pure 1st columns ka elements print ho jyega 
# output [2,5,8]


#sub matrix slicing
# row aur columns dono me range ho 
print(arr2d[0:2, 0:2])
# isse row me 0 se 2nd tk elements aur columns me v 0 se 2nd tk ke elements print ho jynge
#output would be 
#[[1 2], [4,5]]


# slicing with steps
print(arr2d[::2, ::2])
# rows aur columns dono me sare elements target hue h aur dono me 1-1 element skip krke print hoga
# output [[1,3], [7,9]]


# mixing index and slicing
print(arr2d[0, 1:3])
# row 0 aru columns me 1-2 print hoga
#output = [2 3]

print(arr2d[0:2, 2])
#rows 0 aur 1 aur columns me sirf 2 
# output = [3,6]


