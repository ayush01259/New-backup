import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from numpy.random import normal
from numpy import random
import random
from scipy.stats import norm
from sklearn.neighbors import KernelDensity



sample = normal(loc=50, scale=5, size=1000)
print(sample)

historgram = plt.hist(sample, bins=10)
plt.show()
sample_mean = sample.mean()
sample_std = sample.std()
dist = norm(sample_mean, sample_std)

values = np.linspace(sample.min(),  sample.max(), 100)
probabilities = [dist.pdf(value) for value in values]

plt.hist(sample, bins=10, density=True)
plt.plot(values, probabilities)
plt.show()

sample1 = normal(loc=20, scale=5, size=300)
sample2 = normal(loc=40, scale=5, size=700)
samplle = np.hstack((sample1, sample2))
plt.hist(samplle, bins=50)
plt.show()

model = KernelDensity(bandwidth=1, kernel='gaussian')
# converting the data into 2d array
samplle = samplle.reshape((len(samplle), 1))
model.fit(samplle)

values  = np.linspace(samplle.min(), samplle.max(), 100)
values = values.reshape((len(values), 1))

probabilities = model.score_samples(values)
probabilities = np.exp(probabilities)

plt.hist(samplle, bins=50, density=True)
plt.plot(values[:],probabilities)
plt.show()