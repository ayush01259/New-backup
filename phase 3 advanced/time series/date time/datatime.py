import pandas as pd
import datetime
data = {
    "Date": ["2023-01-05", "2023-02-10", "2023-03-15", "2023-04-20"],
    "Product": ["Laptop", "Shoes", "Phone", "Laptop"],
    "Sales": [50000, 2500, 18000, 52000]
}

df = pd.DataFrame(data)


# step 1 : Making string date into actual date 
df["Date"] = pd.to_datetime(df["Date"])
print(df)

# step 2 : Extract dates parts
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["Day_name"] = df["Date"].dt.day_name()
print(df)

# step 3 : Monthly sales summary ( very important )
monthly_sales = df.groupby("Month")["Sales"].sum()


print("\n \n Monthly sales : \n \n ",monthly_sales)


# sorting by date
df = df.sort_values("Date")


# step 4 : time based filtering 

# set to march only
march_data = df[df["Month"] == 3]

# data range
data_range = df[(df["Date"]>= "2023-02-01") & (df["Date"]<= "2023-03-31")]

print(data_range)