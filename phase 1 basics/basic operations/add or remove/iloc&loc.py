import pandas as pd
data = {
    "Name": ["Aman", "Ravi", "Neha", "Priya"],
    "Age": [15, 16, 14, 15],
    "Grade": ["B", "A", "C", "A"]
}

df = pd.DataFrame(data)

# using iloc to print the value of 2nd row and 2nd column
print("2nd row and 2nd column:\n", df.iloc[1:2,1:2])

# using loc to pirnt name and grade columns 
print("Name and grade column:\n", df.loc[:, ["Name" , "Grade"]])

# using iloc to print strting 3 rows and 2 columns
print("First 3 rows nd 2 cols:\n", df.iloc[:3, :2])