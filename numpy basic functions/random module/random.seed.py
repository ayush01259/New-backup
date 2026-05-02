import numpy as np
np.random.seed(42)
print(np.random.rand(3))

# yeh random numbers ko reproducible bnata h mtlb ek baar ek trh ka seed bna die to dobara whi seed same output dega na ki alg alg
np.random.seed(49)
print(np.random.rand(4))