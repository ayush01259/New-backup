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

# plot 1 : countplot() --> har region ke orders
plt.figure(figsize=(6,4))
sns.countplot(x="Region", data=df)
plt.title("Number of Orders per Region")
plt.show()

# plot 2 : boxplot() --> region kki sales spread
plt.figure(figsize=(6,4))
sns.boxplot(x="Region", y="Sales",  data=df)
plt.title("Sales Dsitribution Across Regions")
plt.show()



plt.figure(figsize=(6,5))
sns.countplot(x="Product", data=df)
plt.title("Products wise Orders")
plt.show()



plt.figure(figsize=(7,4))
sns.boxplot(x="Salesperson", y="Sales", data=df)
plt.title("Salesperson wise Sales")
plt.show()

