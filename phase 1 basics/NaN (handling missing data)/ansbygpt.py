import pandas as pd
import numpy as np

data = {
    "Name" : ["Aman", "Ravi", "Neha", "Priya", "Arjun"],
    "Age": [20, 25, np.nan, 22, None], 
    "Marks" : [85, np.nan, 74, 90, 88],
    "City": ["Delhi", None, "Mumbai", "Delhi", "Kolkata"]
}

df = pd.DataFrame(data)
print(df)

#1 printing missing row data
print("Missing data in row:\n", df.notnull())
print("Missing data in datasheet:\n", df.isnull())
print("Rows with missing values:\n", df[df.isnull().any(axis=1)])

#2 counting no of missing values in columns
print("No of missing values in per column:\n", df.isnull().sum())

#3 filling Unknown in NaN
df[["Name", "City"]] = df[["Name", "City"]].fillna("Unknown")
print("After filling Unknown in Name & City:\n", df)

#4 filling NaN in Age by average Age
df["Age"].fillna(df["Age"].mean(), inplace=True)
print("After filling Age NaN with mean:\n", df)

#5 replacing NaN in Marks by median
df["Marks"].fillna(df["Marks"].median(), inplace=True)
print("After filling Marks NaN with median:\n", df)

#6 removing rows where NaN >1
print("Rows with at most 1 NaN:\n", df[df.isnull().sum(axis=1) <= 1])
