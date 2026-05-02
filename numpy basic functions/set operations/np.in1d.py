import numpy as np 
a = np.array([6,2,9,4,5,8])
b = np.array([1,2,3,3,4,5])
print("Checking elements of a are present in b or not :", np.in1d(a , b))

# yeh a ko b se compare krta h then a me jo elements b me rhta h khi v to usse true khta h aur nhi rhta h toh usse false de deta hai