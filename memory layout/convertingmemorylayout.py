#to convert normal into fortan order
import numpy as np
# arr = np.array([[21,49,49],
#                 [14,25,36]])
# print(arr)
# print(arr.flags)

# arr_for = np.asfortranarray(arr)
# print(arr_for.flags)


# to convert normal into contiguous order
asdf = np.arange(1,25).reshape(4,6)
print(asdf)
print(asdf.flags)
asdf_cont = np.ascontiguousarray(asdf)
print(asdf_cont.flags)