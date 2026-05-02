# vector l1 aur l2 norm manually aur np dono se calculate krke verify krna h 
import numpy as np
A = np.array([3,5,7])
l1 = np.linalg.norm(A, 1)
l2 = np.linalg.norm(A,2)

print(l1)
print(l2)

l1_man = abs(3) + abs(5) + abs(7)
l2_man = (3**2 + 5**2 + 7**2) ** 0.5

print(l1_man)
print(l2_man)