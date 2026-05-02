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
# more clear way to do this
print("Rows with missing values:\n", df[df.isnull().any(axis=1)])



#2 counting no of missing values in columns
print("No of missing values in per column:\n", df.isnull().sum())

#3  filling unknown in NaN
print("Fillin unknown in NaN:\n", df.fillna("Unknown"))
# more clear way
print("Filling Unknown in NaN in name and city:\n", df[["Name", "City"]] == df[["Name", "City"]].fillna("Unknown"))

#4 filling nan in age by average age
print("Filling NaN in Age:\n", df["Age"].fillna(df["Age"].mean()))
# to make this changes in the data 
print(df["Age"].fillna(df["Age"].mean(), inplace=True))

#5 replacing NaN values in marks by median
print("Replacing NaN in marks by median:\n", df["Marks"].fillna(df["Marks"].median()))
# to make this permanent
print(df["Marks"].fillna(df["Marks"].median(), inplace=True))


#6 removing rows where NaN >1
print("Removing rows with multiple NaN:\n", df[df.isnull()])



