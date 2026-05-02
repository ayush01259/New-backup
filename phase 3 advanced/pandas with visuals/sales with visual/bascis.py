import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")  # Graph ka background clean & professional

data = {
    "Salesperson": ["Ravi", "Neha", "Amit", "Ravi", "Amit", "Neha", "Simran", "Simran"],
    "Region": ["North", "South", "East", "North", "West", "South", "West", "East"],
    "Product": ["Laptop", "Shoes", "Laptop", "Phone", "Shoes", "Phone", "Phone", "Laptop"],
    "Sales": [50000, 1200, 45000, 18000, 2500, 22000, 19000, 52000],
    "Quantity": [1, 3, 2, 1, 4, 2, 1, 3]
}

df = pd.DataFrame(data)

# bar plot
plt.figure(figsize=(7,4))
sns.barplot(x="Salesperson", y="Sales", data=df, estimator=sum)
plt.title("Total Sales by Salesperson")
plt.show()

# line plot 
df["Order_No"] = range(1, len(df)+1)

plt.figure(figsize=(7,4))
sns.lineplot(x="Order_No", y="Sales", data=df, markers="0")
plt.title("Sales Trend Across Orders")
plt.show()


# Scatter Plot == relationship / correlation 

plt.figure(figsize=(7,4))
sns.scatterplot(x="Quantity", y="Sales", hue="Product", data=df, s=100)
plt.title("Sales vs Quantity (Product Wise)")
plt.show()