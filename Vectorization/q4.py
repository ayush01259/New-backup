import numpy as np

arr = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])

#adding 10 to each element using loop
add = []
for x in arr:
    add.append([i+10 for i in x])
add = np.array(add)

print(add)


# by vectorization
print(arr + 10)