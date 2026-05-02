import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.DataFrame({
    "Sales": [12000, 15000, 18000, 13000, 90000, 16000, 17000, 15500],
    "Quantity": [1,2,2,1,10,2,2,1],
    "Region": ["North","South","North","East","West","South","East","North"],
    "Product": ["A","B","A","C","A","B","C","A"]
})


print(df)
 
print(df.describe())
print(df.shape)
print(df.head())
print(df.info())
sns.boxplot(y=df["Sales"])
plt.title("Sales distribution ( outlier detection )")
plt.show()

sns.boxplot(x="Region", y="Sales", data=df)
plt.title("Region wise sales distribution")
plt.show()

sns.countplot(x="Product", data=df)
plt.title("Product Frequency")
plt.show()
sns.countplot(x="Product", data=df)
plt.title("Count of orders per product")
plt.show()
sns.scatterplot(x="Quantity", y="Sales", data=df, hue="Region", s=100)
plt.title("Sales vs quantity by region")
plt.show()