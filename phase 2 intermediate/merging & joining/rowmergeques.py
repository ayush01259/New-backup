# here are some hard qeustions on row merge 
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

customer_details = {
    "CID" : [1,2,3,4], 
    "Customer_Name" : ["Ravi", "Neha", "Amit", "Simran"], 
    "Phone" : ["9999", "8888", "7777", "6666"]
}

df_cust_details = pd.DataFrame(customer_details)

merged = df_cust_details.merge(df_orders, left_on="CID", right_on="CustomerID", how="inner")
print(merged)

# merging multiple keys
sales = {
    "Region" : ["North", "South", "East", "West"], 
    "Product" : ["Laptop", "Phone", "Shoes", "Laptop"], 
    "Sales" : [50000, 30000, 1200, 45000]
}

target = {
    "Region" : ["North", "South", "East", "West"], 
    "Product" : ["Laptop", "Phone", "Shoes", "Laptop"], 
    "Target" : [4000, 28000, 1000, 50000]
}

df_sales = pd.DataFrame(sales)
df_target = pd.DataFrame(target)

mutli_key_merged = df_sales.merge(df_target, on=["Region", "Product"], how="inner")
mutli_key_merged["Achieved"] = mutli_key_merged["Sales"] >= mutli_key_merged["Target"]
print("\n multi key merging in sales with target on the basis of region and product \n \n", mutli_key_merged)


# Concantenation ( row wise )
north_df = pd.DataFrame({
    "Salesperson" : ["Ravi9", "Neha"], 
    "Region" : ["North", "North"],
    "Sales" : [50000, 43000]
})

south_df = pd.DataFrame({
    "Salesperson" :["Amit", "Simran"], 
    "Region" : ["South", "South"], 
    "Sales" : [35000, 37000]
})

merged_rows = pd.concat([north_df, south_df], ignore_index=True)
print("/n adding rows : \n",merged_rows)

# concantenation ( column wise )

df1 = pd.DataFrame({
    "Product" : ["Laptop", "Phone", "Shoes"],
    "Price" :[50000, 14000, 1200]
})

df2 = pd.DataFrame({
    "Stock" : [50, 200, 300], 
    "Category" : ["Electronics", "Electronics", "Clothing"]
})

merged_cols = pd.concat([df1, df2], axis=1)
print("Adding cols :\n \n", merged_cols)

print(customer_details)

