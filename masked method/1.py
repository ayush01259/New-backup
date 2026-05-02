# A Masked Array is a special NumPy array where some values are marked as invalid or missing.

# Useful when dealing with real-world datasets (with NaN, missing, or placeholder values).

# Implemented using numpy.ma module.

import numpy as np
import numpy.ma as ma
# question 1 : maksing all 999 values and calculate the mean
data = np.array([1,2,999,4,5])
mask = ma.masked_equal(data, 999)
print(mask)
print(mask.mean())


