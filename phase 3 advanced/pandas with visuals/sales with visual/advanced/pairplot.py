import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")

data = {
    "Salesperson": ["Ravi", "Neha", "Amit", "Ravi", "Amit", "Neha", "Simran", "Simran"],
    "Region": ["North", "South", "East", "North", "West", "South", "West", "East"],
    "Product": ["Laptop", "Shoes", "Laptop", "Phone", "Shoes", "Phone", "Phone", "Laptop"],
    "Sales": [50000, 1200, 45000, 18000, 2500, 22000, 19000, 52000],
    "Quantity": [1, 3, 2, 1, 4, 2, 1, 3]
}

df = pd.DataFrame(data)

df_encoded = df.copy()
for col in ["Region", "Product", "Salesperson"]:
    df_encoded[col] = df_encoded[col].astype("category").cat.codes

print(df_encoded.head())

# sns.pairplot(df_encoded, hue="Product", diag_kind="kde", palette="husl")
sns.pairplot(df_encoded, hue="Region", corner=True, palette="coolwarm")
plt.suptitle("Pairplot of Encoded Sales Datasheet ",y=1.02)
# plt.suptitle is used for global title ( since it makes its own figure )
plt.show()