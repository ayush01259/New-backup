import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from numpy.random import normal
from numpy import random
import random
L = [ ]
for i in range(10000):
    L.append(random.randint(1,6))

print(len(L))
print(L[:5])


suum = (pd.Series(L).value_counts()/pd.Series(L).value_counts().sum()).sort_index()
print(suum)
sns.barplot(x=suum.index, y=suum.values)
plt.show()

sample = normal(loc=50, scale=5, size=1000)