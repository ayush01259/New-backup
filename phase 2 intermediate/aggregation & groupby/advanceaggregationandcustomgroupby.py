import pandas as pd

data = {
    "Salesperson": ["Ravi", "Neha", "Amit", "Ravi", "Amit", "Neha", "Simran", "Simran"],
    "Region": ["North", "South", "East", "North", "West", "South", "West", "East"],
    "Product": ["Laptop", "Shoes", "Laptop", "Phone", "Shoes", "Phone", "Phone", "Laptop"],
    "Sales": [50000, 1200, 45000, 18000, 2500, 22000, 19000, 52000],
    "Quantity": [1, 3, 2, 1, 4, 2, 1, 3]
}
# different aggregations per columns 

df = pd.DataFrame(data)
summary = df.groupby("Salesperson").agg({
    "Sales" : ["sum", "mean"],
    "Quantity":"max"
})
print(summary)

#2 custom lambda function for filtering 
custom = df.groupby("Product").agg({
    "Sales": lambda X: round(X.mean()/1000,2),
    "Quantity": "sum"
})
print(custom)


#3 renaming aggregation columns (readable outputs)
renamed = df.groupby("Region").agg(
    Total_Sales = ("Sales", "sum"),
    Avg_Sales = ("Sales", "mean"),
    Total_Quantity = ("Quantity", "sum")
)
print(renamed)


# multi index groupby
multi_group = df.groupby(["Region", "Product"])[["Sales", "Quantity"]].sum()
print("Multiple column  grouping : \n",multi_group )

# reseting index
rest_index= multi_group.reset_index()
print(rest_index)