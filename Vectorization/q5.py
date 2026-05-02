import numpy as np 
import time
arr1 = np.arange(1000000)
arr2 = np.arange(1000000)

start = time.time()
addbyelelement = [arr1[i] + arr2[i] for i in range(len(arr1))]
end = time.time()
total_time = end - start
print("Total time in manual mode", total_time)

start = time.time()
addbyvec = arr1 + arr2
end = time.time()
total_timebyvec = end-start
print("Total time in vecotrizatioin = ", total_timebyvec)