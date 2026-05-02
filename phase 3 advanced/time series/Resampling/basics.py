import pandas as pd

data = {
    "Date": ["2023-01-05", "2023-02-10", "2023-03-15", "2023-04-20"],
    "Product": ["Laptop", "Shoes", "Phone", "Laptop"],
    "Sales": [50000, 2500, 18000, 52000]
}

df = pd.DataFrame(data)

df["Date"]  = pd.to_datetime(df["Date"])
df = df.set_index("Date")

print("Month wise sales : \n", df.resample("M")["Sales"].sum())
print("\n Quater wise sales :\n", df.resample("Q")["Sales"].sum())


