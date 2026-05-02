import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.DataFrame({
    "Price":[120,130,125,140,135,500,150,145,155,600]
})
Q1 = df["Price"].quantile(0.25)
Q2 = df["Price"].quantile(0.75)
IQR = Q2 - Q1

lower = Q1 - 1.5 * IQR
upper = Q2 + 1.5 * IQR

outliers = df[(df["Price"] < lower) | (df["Price"] > upper)]
print(outliers)
print("Mean before removing the outlier \n \n",outliers.mean)

# removing outlers 
remove_outlier = df[(df["Price"]>=lower) & (df["Price"] <= upper)]
print(remove_outlier)
print("Mean after removing the outler \n \n",remove_outlier.mean)

# replacing outlers with clip
df["replaced"] = df["Price"].clip(lower, upper)
print(df)

# visually confirming by boxplot
sns.boxplot(y=df["Price"])
plt.show()

