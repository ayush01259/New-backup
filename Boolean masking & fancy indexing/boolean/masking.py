import numpy as np
arrr = np.array([1,2,3,4,5,6,7,8,9,10])
# masking elements with one condition 
mask = arrr> 5
print("Mask :", mask)
print("Filtered array after masking : \n", arrr[mask])


# masking with multiple conditions
# here we can also use AND (&) or OR(|) condition for more complex filtering

masked = (arrr>4) & (arrr<8)
print("Maksed array: ", masked)
print("Filtered array after masking :", arrr[masked])
