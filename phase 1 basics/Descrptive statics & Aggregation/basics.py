import pandas as pd

data = {
    "Salesperson": ["Ravi", "Neha", "Amit", "Ravi", "Amit", "Neha", "Simran", "Simran"],
    "Region": ["North", "South", "East", "North", "West", "South", "West", "East"],
    "Product": ["Laptop", "Shoes", "Laptop", "Phone", "Shoes", "Phone", "Phone", "Laptop"],
    "Sales": [50000, 1200, 45000, 18000, 2500, 22000, 19000, 52000],
    "Quantity": [1, 3, 2, 1, 4, 2, 1, 3]
}
df = pd.DataFrame(data)
print(df)

# to find the mean (average)
print("Average sales: ", df["Sales"].mean())
print("Average quantity:\n", df["Quantity"].mean())



# to print median ( middle values )
print("Median sales:", df["Sales"].median())


# mode ( most frequesnt values )
print("Most frequent region:", df["Region"].mode()[0])


# sum / max / min/ count
print("Total sales: \n", df["Sales"].sum())
print("Highest sales:\n", df["Sales"].max())
print("Lowest sales:\n", df["Sales"].min())
print("Total rows:\n", df["Sales"].count())



# describing the full summary of the dataframe
print("Full summary of the Numeric columns:\n", df.describe())


# value counts ( for categorical frequency )
print("Salesperson frequency : \n", df["Salesperson"].value_counts())