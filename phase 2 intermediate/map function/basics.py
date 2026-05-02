import pandas as pd

df = pd.DataFrame({
    "Name": ["Ravi", "Neha", "Amit", "Simran"],
    "Sales": [50000, 12000, 45000, 32000],
    "Region": ["North", "South", "East", "West"]
})

print(df)

# map() -> single columnns transformation (used mainly for values replacement)
# using it to converting region into short code
region_map = {
    "North" : "N", 
    "South" : "S", 
    "East": "E", 
    "West" : "W"
}

df["Region_Code"] = df["Region"].map(region_map)
print(df)


# apply () -> row/ column wise function 
df["Sales_in_K"] = df["Sales"].apply(lambda x : x/1000)
print(df)

# row wise apply 
df["Status"] = df.apply(lambda row : "High" if row["Sales"] > 30000 else "Low", axis=1)
print(df)

# applymap() -> entire dataframe 
# jab sab cell pr function lgana hota to use krte iska
df_num = df[["Sales", "Sales_in_K"]]
df_num = df_num.applymap(lambda x : round(x, 2))
# ab applymap ke jgh map v use kr skte h applymap ke jgh map v kaam krega
#  

print(df_num)

# apply (axis = 1)
df["Customer_Type"] = df.apply(
    lambda row: "VIP" if (row["Sales"] > 40000 and row["Region"] == "North") else "Normal",
    axis=1
)
print(df)
