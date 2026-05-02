import pandas as pd

df = pd.read_csv("./PANDAS/phase 1 basics/intro/students.csv")
print(df.head())

print("\nINFo: \n")
print(df.info())

# descriptive statics 
print("\nDescription: \n", df.describe())

#shape (rows, columns)
print("\nShape: ", df.shape)

# columns
print("\nColumnns: ", df.columns)

# ek columns select krna (series me)
print("\nMarks column: \n", df['Marks'])

# multiple columns selection (data frame)
print("\nName + Marks :\n", df[['Name', 'Marks']])

#ek row (loc by index)
print("\nRow 2:\n", df.loc[2])

# multiple rows (slice)
print("\nFirst 3 rows: \n", df[0:3])