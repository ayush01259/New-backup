import numpy as np 
a = np.array([10,20,30,40,50])
b = np.array([30,40,50,60,70])


print("Union of two:", np.union1d(a,b))
print("Intersection of a and b:", np.intersect1d(a,b))
print("Difference between a and b :", np.setdiff1d(a,b))
print("Difference between b and a: ", np.setdiff1d(b ,a))
