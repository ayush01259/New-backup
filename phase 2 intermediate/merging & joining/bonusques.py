import pandas as pd

customers = {
    "CustomerID": [1, 2, 3, 4],
    "Name": ["Ravi", "Neha", "Amit", "Simran"],
    "City": ["Delhi", "Mumbai", "Kolkata", "Chennai"]
}
orders = {
    "OrderID": [101, 102, 103, 104, 105],
    "CustomerID": [1, 2, 1, 3, 5],
    "Amount": [5000, 7000, 9000, 3000, 8000]
}

df_customers = pd.DataFrame(customers)
df_orders = pd.DataFrame(orders)

# ✅ Step 1: Left join (all customers, even if no order)
merged = df_customers.merge(df_orders, on="CustomerID", how="left")

# ✅ Step 2: Summary per customer
summary = merged.groupby(["CustomerID", "Name", "City"]).agg(
    Total_Orders=("OrderID", "count"),
    Total_Sales=("Amount", "sum"),
    Avg_Order_Value=("Amount", "mean")
).reset_index()

# ✅ Step 3: Replace NaN for customers with no orders
summary = summary.fillna({"Total_Sales": 0, "Avg_Order_Value": 0})

print(summary)


# a question that combine order data and gives summary table of every customer that includes total order count , total sales, average order amount, city

import pandas as pd
customers = {
    "CustomerID" : [1,2,3,4],
    "Name" : ["Ravi", "Neha", "Amit", "Simran"],
    "City" : ["Delhi", "Mumbai", "Kolkata", "Chennai"]
}

orders = {
    "OrderID" : [101, 102,103, 104, 105], 
    "CustomerID" : [1, 2, 1, 3 ,5],
    "Amount" : [5000, 7000, 9000, 3000, 8000]
}

df_customers = pd.DataFrame(customers)
df_orders = pd.DataFrame(orders)

# step 1 -> left join 
merged = df_customers.merge(df_orders, on="CustomerID", how="left")

# step 2 -> Sumamry per customer
summary = merged.groupby(["CustomerID", "Name", "City"]).agg(
    Total_Orders = ("OrderID", "count"), 
    Total_Sales=("Amount", "sum"),
    Avg_Order_Value = ("Amount", "mean")
).reset_index()

# step 3 -> Replacing NaN for customers with no orders
summary = summary.fillna({"Total_Sales": 0, "Avg_Order_Vale":0})
print(summary)