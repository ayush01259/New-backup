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

# Only numeric columns ke liye correlation
# corr = df.corr()
# print(corr)

corr = df.select_dtypes(include=['number']).corr()
print(corr)
# corr sirf integers ya floats ke lie h yeh strings pr work nhi krta islie hm yeh code use krrhe warna upr wale corr = df.corr() use kr skte hai 


df_encoded = df.copy()
df_encoded["Region"] = df_encoded["Region"].astype("category").cat.codes

df_encoded["Product"] = df_encoded["Product"].astype("category").cat.codes

df_encoded["Salesperson"] = df_encoded["Salesperson"].astype("category").cat.codes

corrr = df_encoded.corr()
print(corrr)

plt.figure(figsize=(6,4))
sns.heatmap(corrr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()
# cmap se color define hota visual ka, first wla corrr function h jsse display krna h visuals me, annot = true number likh deta hai,  linewidht se box ke beech ka width aata
sns.pairplot(df)
plt.show()



