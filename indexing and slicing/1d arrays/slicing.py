import numpy as np
arr = np.array([10,20,30,40,50])

print(arr[1:4])
# to print from the 1st index to the 4th index 
# it would give the output as [20,30,40]


print(arr[:3])
# yeh strt to 0th index se krega pr end 3rd index pr krega 
# it would give the output as [10,20,30] 3rd index limit h to wo count nhi hoga 



print(arr[2:])
# yeh start to 2nd index mtlb 3rd element se krega pr end array ke end ke sath hoga 
# the output would look like [30,40,50]


print(arr[::2])
# isse sare elements to print hote h pr 1 ko skip krte hue means yeh sare elements ko select krta h aur 1 skip krte hue print krte chale jata h 
# output will be [10,30,50]


print(arr[::-1])
# yeh mainly array ko reverse kr deta h bcz sare elements to target ho hi rhe aur - last se chlta h 
#output will be [50,40,30,20,10]