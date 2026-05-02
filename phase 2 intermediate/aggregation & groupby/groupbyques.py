import pandas as pd

data = {
    "Salesperson": ["Ravi", "Neha", "Amit", "Ravi", "Amit", "Neha", "Simran", "Simran"],
    "Region": ["North", "South", "East", "North", "West", "South", "West", "East"],
    "Product": ["Laptop", "Shoes", "Laptop", "Phone", "Shoes", "Phone", "Phone", "Laptop"],
    "Sales": [50000, 1200, 45000, 18000, 2500, 22000, 19000, 52000],
    "Quantity": [1, 3, 2, 1, 4, 2, 1, 3]
}
df = pd.DataFrame(data)
print(df)

#ques1 total and average sales of every salesperson
print("\nAverage and total sales per salesperson\n",df.groupby("Salesperson")["Sales"].agg(["mean","sum"]))

# ques 2 total quantity sold in every region
print("\nTotal quantity sold in every region:\n", df.groupby("Region")["Sales"].sum())

# ques 3 most sold product
print("\nMost sold product:\n", df.groupby("Product")["Sales"].sum())

# ques 4 total sales on the basis of region and product
print("\n total sales on the basis of region and product\n", df.groupby(["Region", "Product"])["Sales"].sum())

# ques 5: a summary where  for every region we have sum , mean, and max sales 
print("\nMaking summary :\n",df.groupby("Region")["Sales"].agg(["sum", "mean", "max"]))