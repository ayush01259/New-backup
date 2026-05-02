import numpy as np
import numpy.ma as ma

# question 1 : maksing all 999 values and calculate the mean
data = np.array([1,2,999,4,5])
mask = ma.masked_equal(data, 999)
print(mask)
print(mask.mean())


# qustion 2: custom masking 
data = np.array([10, 20, 30, 40, 50])
mask = ma.masked_equal(data, 0,1,0,1,0)
print(mask)

# question 3: masking -99 and then fnding the average temparture
temp = np.array([25, 30, -99, 28, 27, -99])
masked_temp = ma.masked_equal(temp, -99)
print(masked_temp.mean())
# question 4: replacing the masked value with the average temparature
fill_temp = masked_temp.filled(temp.mean())