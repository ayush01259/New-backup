import pandas as pd
data = {
    "Name": ["Aman", "Ravi", "Neha", "Priya"],
    "Age": [15, 16, 14, 15],
    "Grade": ["B", "A", "C", "A"]
}

df = pd.DataFrame(data)
print("Before adding :\n",df )
# adding a new column named marks
df["Marks"] = [74, 92, 63, 89]

print(df)


# removing grades (temporarily)
df = df.drop("Grade", axis=1 ) 
print("after removing grades:\n",df)
# to remove anything permanently 
df = df.drop("Age", axis=1, inplace=True)
print("after permanently removing age:\n",df)