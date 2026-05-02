import pandas as pd
data = {
    "Salesperson" : ["Ravi", "Neha", "Amit", "Ravi", "Amit", "Neha", "Simran", "Simran"], 
    "Region": ["North", "South", "East", "North", "West", "South", "West", "East"],
    "Product":["Laptop", "Shoes", "Laptop", "Phone", "Shoes", "Phone", "Phone", "Laptop"],
    "Sales":[50000, 1200, 45000, 18000, 2500, 22000, 19000, 52000], 
    "Quantity":[1,3,2,1,4,2,1,3]
}
df= pd.DataFrame(data)
print(df)

# syntax
# df.groupby("ColumnName")["TargetColumn"].operation()


# total sales by region 
print(df.groupby("Region")["Sales"].sum())

# average sales per person 
print(df.groupby("Salesperson")["Sales"].mean())

# quantity sold per product
print(df.groupby("Product")["Quantity"].sum())

# mutliple aggregations together
print(df.groupby("Region")[["Sales", "Quantity"]].agg(["sum", "mean", "max"]))

# groupby multiple columns
print(df.groupby(["Region", "Salesperson"])["Sales"].sum())

# reset index ( for cleaner datagrame output)
region_sales = df.groupby("Region")["Sales"].sum().reset_index()
print(region_sales)