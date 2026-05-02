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

#q1 average, mdian and total sales of the datasheet

# finding average
print("The average sala in the datasheet: \n", df["Sales"].mean())

# median sales of thddatasheet
print("The median sales of the datasheet :\n", df["Sales"].median())

# total sales of the datasheet 
print("Total sales of the datasheet:\n", df["Sales"].sum())


# q2 most sale of a specific product based on frequency
print("most sales based on frequency:\n", df["Product"].mode()[0])

# q3 most quantity sold by a salesperson
sales_by_person = df.groupby("Salesperson")["Quantity"].sum()
print("Total quantity sold by each salesperson: \n", sales_by_person)
print("Salesperson with max quantity sold:\n", sales_by_person.idxmax())

# question 4 no of unique regions
print("Number of unique regions:\n", df["Region"].unique())

# question 5 total sales of teh entire datasheet
print("Total sales of the datasheet:\n", df["Sales"].sum())