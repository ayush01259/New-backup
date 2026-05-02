#ccreating two arrays and then adding them from manual way and using vectorization 
import numpy as np
array_1 = np.array([1,2,3,4,5])
array_2 = np.array([10,20,30,40,50])

#adding them in manual way


sumoftwo = [int(array_1[i] + array_2[i]) for i in range(len(array_1))]
# for i in range(len(array_1)):
#     sumoftwo.append(array_1[i] + array_2[i])

print("Sum of array 1 and array 2 in manual way are :", sumoftwo)

#adding them in vectorization
vectro_method = array_1 + array_2 
print("Sum of array 1 and array 2 in vectorization way are :", vectro_method)