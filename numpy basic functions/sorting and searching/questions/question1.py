import numpy as np 
arr = np.array([15,42, 7 , 23,  89, 34])
print("Ascending sorting", np.sort(arr))
print("Ascending sorting index:", np.argsort(arr))
print("Descending sorting :", np.sort(arr)[::-1])
print("Descending sorting index: ", np.argsort(arr)[::-1])