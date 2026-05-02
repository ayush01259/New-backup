# python cleaning tools 
import pandas as pd
data = {
    "Name" : ["Aman", "Ravi"],
    "Age": [20, 25]
}
df = pd.DataFrame(data)

# renaming a column
df.rename(columns={"Name":"Students_Name"}, inplace=True)
print(df)

# changiing data types
df["Age"] = df["Age"].astype(float)
print(df.dtypes)

# replacing values
df["Students_Name"] = df["Students_Name"].replace("Aman", "Amar")
print(df)

# dropping duplicates
df = pd.DataFrame({
    "Name":["Aman", "Ravi", "Aman", "Ravi"],
    "Age":[20, 25, 20, 25]
})
print("Before:\n", df)
 
df = df.drop_duplicates()
print("After:\n", df)

# sorting data
df = pd.DataFrame({
    "Name":["Aman","Ravi","Neha"],
    "Marks":[80,95,70]
})
print(df.sort_values(by="Marks", ascending=False))

#reseting index
df = df.sort_values(by="Marks", ascending=False)
df.reset_index(drop=True, inplace=True)
print("reseting index:\n",df)