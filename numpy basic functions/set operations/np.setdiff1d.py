import numpy as np
a = np.array([1,2,3,4,9,6,3,5,3,8,2])
b = np.array([1,2,3,2,3,4,5,5,6,7,8])

print("Difference in a - b =", np.setdiff1d(a, b))
#it returns the element difference in a and b, so in a 9 is present but in b its not thats why the output is 9
print("difference in b- a = ", np.setdiff1d(b, a))
# here also in b there is 7 but in a its not present so the output here is 7



