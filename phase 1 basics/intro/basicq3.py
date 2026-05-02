# here we have to just import a csv file using absolute path 
import pandas as pd
import csv
# by using index_col = false to index reset ho jata h jisse koi csv file ka index weird nhi aaye
data = pd.read_csv("./PANDAS/phase 1 basics/intro/students.csv", index_col=False)
print(data)
# printing top 3 rows
print("The top 3 rows:\n", data.head(3))

 # printing column names 
print("Column names:\n", data.columns)

# printing  all stats by describe
# if we use include = 'all' then categorical and numerical sare print ho jynge summary me
print(data.describe(include='all'))