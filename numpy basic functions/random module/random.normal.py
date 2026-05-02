# #normal distribution (Gaussian distribution) ke random numbers generate krta hai 
# #format normal(mean, std, size)

# import numpy as np
# print("Normal distribution:", np.random.normal(0,1,5))


# # example of normal distribution
# mean = 50
# std_dev = 10
# size = 100

# data = np.random.normal(mean, std_dev, size)
# print("First ten values : ", data[:10])

# print("Calcualted mean : ", np.mean(data))
# print("Calculated std dev: ", np.std(data))



import numpy as np
import matplotlib.pyplot as plt

# Parameters
mean = 50
std_dev = 10
size = 1000

# Generate random numbers
data = np.random.normal(mean, std_dev, size)

# Stats check
print("Calculated Mean:", np.mean(data))
print("Calculated Std Dev:", np.std(data))

# Plot histogram
plt.hist(data, bins=30, color='skyblue', edgecolor='black', density=True)
plt.title("Normal Distribution (mean=50, std=10)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
