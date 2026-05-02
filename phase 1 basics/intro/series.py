import pandas as pd
# single column 
S = pd.Series([10,20,30,40,50])
print(S)

# Multi columns (dataframe)
data = {
    "Name": ["Ravi", "priya","AMAN"],
    "Class":[10,10,10],
    "Marks":[80,81,91]
}
df = pd.DataFrame(data)
print("Multi column data:\n", df)
print(df.info())
# print(df["Name"])
# print(df["Name","Marks"])
print("\n",df["Name"])
print("\n \n",df[["Name", "Marks", "Class"]])