import numpy as np
# arr = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])

# #manual way to add column wise
# col_sum = [int(sum(arr[:, i])) for i in range(arr.shape[1])]
# print("Adding columns manually", col_sum)

# # adding by vectorization

# print("By vecotrization : ", arr.sum(axis= 0))


data = np.array([15, 20, 25, 30, 35, 40])

# mean & std
mean = data.mean()
std = data.std()

# ----- Loop way -----
normalized_loop = []
for x in data:
    normalized_loop.append(int((x - mean) / std))

print("Normalization (loop):", normalized_loop)

# ----- Vectorized way -----
normalized_vec = (data - mean) / std
print("Normalization (vectorized):", normalized_vec)