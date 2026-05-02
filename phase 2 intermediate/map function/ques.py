import pandas as pd
df = pd.DataFrame({
    "Name": ["Ravi", "Neha", "Amit", "Simran"],
    "Sales": [50000, 12000, 45000, 32000],
    "Region": ["North", "South", "East", "West"]
})
 
 #q1 doing every name in uppercase
upper = df["Name"].apply(lambda x : x.upper())

df["upper"] = upper
print(df)


# q2 permium for 40000 above sales else regular
if_else = df.apply(lambda row: "Premium" if row["Sales"]>40000 else "Regular", axis=1) 
df["Status"] = if_else
print(df)

# q3 making new column as bonus = sales * 0.10
df["Bonus"] = df["Sales"].apply(lambda x : x * 0.10)
print(df)
df["Bonus"] = df["Sales"] * 0.10
print(df)
df["Bonus"] = df["Sales"].map(lambda X : X * 0.10)
print(df)