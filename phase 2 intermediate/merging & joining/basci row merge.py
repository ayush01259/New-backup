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

print(df_customers)
print(df_orders)


# inner join ( merges matching customer id )
inner_join = df_customers.merge(df_orders, on="CustomerID", how="inner")
print(inner_join)

# left join  ( keep all customerss )
left_join = df_customers.merge(df_orders, on="CustomerID", how="left")
print("\n",left_join)

# Right join ( all orders + matching customers)
right_join = df_customers.merge(df_orders, on="CustomerID", how="right")
print("\n", right_join)

# outer join ( merges all rows from both sides )
outer_join = df_customers.merge(df_orders, on="CustomerID", how="outer")
print("\n", outer_join)