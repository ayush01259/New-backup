import pandas as pd
df = pd.read_csv('./PANDAS/phase 1 basics/intro/students.csv')

# to print the top 5 rows of the data
print("The top 5 rows of data:\n",df.head())


# to print the last 5 rows of the data
print("The bottom 5 rows of the data:\n",df.tail() )

#to print the total rows and columns of the data
print("Total rows and columns of the data are:\n", df.shape)

# to print the column names of the data 
print("Column names of the data:\n", df.columns)

# to print the dataset summary
print("dataset summary:\n",  df.info())

# to print the stats of the datasheet like std, mean, max, min 
print("The stats of the data are:\n", df["Class"].describe())


# for a specific columns
print("specific column:\n\n",df["Class"])


#filtering class only 10
print("Only 10th class:\n\n", df[df["Class"]>=10])