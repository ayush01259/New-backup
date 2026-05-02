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

# detecting missing data
print("Finding NaN:\n", df.isnull())
# yeh NaN value ko True krke output deta h aur normal values ko false

print("Count Nan in columns:\n", df.isnull().sum())
# it gives output by counting no of NaN per column

print("Not Nan :\n", df.notnull())
# yeh NaN ko false aur data ko true output deta h 





# removing missin data
print("Removes Nan row: \n", df.dropna())

print("Removes NaN column:\n", df.dropna(axis=1))




# filling missing data
print("Replacing NaN by Zeros:\n", df.fillna(0))

print("Fill NaN by mean of marks column:\n", df["Marks"].fillna(df["Marks"].mean()))

print("Marking unknown in city as place of NaN :\n", df["City"].fillna("Unknown"))