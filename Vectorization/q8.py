import numpy as np
arr = np.array([[1,2,3], 
               [4,5,6]])

b = np.array([10,20,30])

result_vec = arr + b
print("Broadcasting resutl: ", result_vec)

result_loop = []
for row in arr:
    new_row = []
    for i in range(len(row)):
        new_row.append(row[i] + b[i])
    result_loop.append(new_row)

result_loop = np.array(result_loop)
print("Loop result :", result_loop)