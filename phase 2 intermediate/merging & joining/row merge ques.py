import pandas as pd
import numpy as np 

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

#q1 merginig cstomers and orders by inner join by using customer id
inner_join1 = df_customers.merge(df_orders, on="CustomerID", how="inner")
print(inner_join1)

#q2 show all customers along side their matching orders also fill NaN as No orders
left_join2 = df_customers.merge(df_orders, on="CustomerID", how="left").fillna("No Orders")
print(left_join2)


#q3 show all orders also by attaching customer name and city and fill missing customer name as unknown
right_join3 = df_customers.merge(df_orders, on="CustomerID", how="right")
right_join3["Name"].fillna("Unknown", inplace=True)
right_join3["City"].fillna("Unknown", inplace=True)
print("\n All orders + known customers  \n", right_join3 )

# q4 outer join 
outer_join4 = df_customers.merge(df_orders, on="CustomerID", how="outer", indicator=True)
print(outer_join4)