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

# Encode categories
df_encoded = df.copy()
for col in ["Region", "Product", "Salesperson"]:
    df_encoded[col] = df_encoded[col].astype("category").cat.codes


sns.jointplot(x="Quantity", y="Sales", data=df_encoded, kind="scatter")
plt.show()


sns.jointplot(x="Quantity", y="Sales", data=df_encoded, kind="reg")
plt.show()

sns.jointplot(x="Quantity", y="Sales", data=df_encoded, kind="kde", fill=True, cmap="Reds")
plt.show()

sns.jointplot(x="Product", y="Quantity", data=df_encoded, kind="hex")
plt.show()