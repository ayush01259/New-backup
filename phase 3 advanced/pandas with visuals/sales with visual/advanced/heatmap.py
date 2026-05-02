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
# corr = df.select_dtypes(include=['number']).corr()
# print(corr)
# plt.figure(figsize=(6,4)) 
# sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
# plt.title("Correlation Heatmap")
# plt.show()
df_encoded = df.copy()
for col in ["Region", "Product", "Salesperson"]:
    df_encoded[col] = df_encoded[col].astype("category").cat.codes

corr2 = df_encoded.corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr2, annot=True, cmap="viridis", linewidths=0.5)
plt.title("Full Dataset Correlation Heatmap (Encoded)")
plt.show()


plt.figure(figsize=(8,7))
sns.heatmap(df_encoded.corr(), annot=True, cmap="YlGnBu", linewidths=0.4)
plt.title("Landis fandis checkup")
plt.show()