#array me se random elements select krta hai
import numpy as np
arr = np.array([10,20,30,40,50])
print("Single choice:", np.random.choice(arr))
print("Multiple choice:", np.random.choice(arr, size=3))
# with probability
print("choice:", np.random.choice(arr, size=3, p=[0.1, 0.2, 0.3,0.2, 0.2]))