import pandas as pd

data = {
    "Date": ["2023-01-05", "2023-02-10", "2023-03-15", "2023-04-20"],
    "Product": ["Laptop", "Shoes", "Phone", "Laptop"],
    "Sales": [50000, 2500, 18000, 52000]
}

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])
# q1 quarter 
df["Quarter"] = df["Date"].dt.quarter
print(df)
df["Month"] = df["Date"].dt.month
# q2 which month had the highest total sales
highest = df.groupby("Month")["Sales"].sum().idxmax()
print(highest)

# q3 laptop sales in march 
laptops_sales = df[(df["Month"] == 3) & (df["Product"] == "Laptop")]
print(laptops_sales)

# q2 me changes to make it better
# we can do month map to highest look better 
month_map = {
    1: "January" , 2: "February", 3: "March", 4:"Apilr", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October" , 11:"November", 12:"December"
}
print(month_map[highest])

# one more pro tip
df["Month_Name"] = df["Date"].dt.strftime("%b")
# it will give Jan , Feb, Mar type of results

df["Month_Full"] = df["Date"].dt.strftime("%B")
# it will give January, February, March type of results