import numpy as np
arr = np.array([5,10,15,20,25])

arrmult = []
for x in arr:
    arrmult.append(int(x * 5))

print("Array mult by 5: ", arrmult)

#vectorization 
arrmvec = arr * 5
print("Also array mult by 5 but by vectorization : ", arrmvec)

arrvecmec = np.multiply(arr, 5)
print("Now by another method :", arrvecmec)
