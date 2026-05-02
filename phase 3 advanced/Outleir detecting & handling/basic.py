import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Sales": [10, 12, 11, 13, 9, 95]
})

Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["Sales"] < lower) | (df["Sales"] > upper)]
print(outliers)

# To remove the outliers 
clean_df = df[(df["Sales"] >= lower) & (df["Sales"]<=upper)]
print(clean_df)
# it will print the dataset without the outlier

# to replace outlier (capping / winsorizing )
df["Sales_Capped"] = df["Sales"].clip(lower, upper)
print(df)

# replacing with mean or median 
df["Price"] = df["Sales"].mask(df["Sales"]> upper, df["Sales"].median())
print("\n \n replaced with median   \n \n ",df)
sns.boxplot(y=df["Sales"])
plt.show()


# df = pd.DataFrame({
#     "Price":[120,130,125,140,135,500,150,145,155,600]
# })

# mean = df["Price"].mean()
# std = df["Price"].std()

# df["Zscore"] = (df["Price"] - mean) / std

# outliers = df[df["Zscore"].abs() > 3]
# print(outliers)