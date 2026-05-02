import pandas as pd

data = {
    "Salesperson": ["Ravi", "Neha", "Amit", "Ravi", "Amit", "Neha", "Simran", "Simran"],
    "Region": ["North", "South", "East", "North", "West", "South", "West", "East"],
    "Product": ["Laptop", "Shoes", "Laptop", "Phone", "Shoes", "Phone", "Phone", "Laptop"],
    "Sales": [50000, 1200, 45000, 18000, 2500, 22000, 19000, 52000],
    "Quantity": [1, 3, 2, 1, 4, 2, 1, 3]
}

df = pd.DataFrame(data)

cross = pd.crosstab(df["Region"], df["Product"])
print(cross)



#q1 creating a pivot table that shows average sales per person 
pivotq1 = df.pivot_table(values="Sales", index="Salesperson", aggfunc="mean")
print("Avg sales per salesperson: \n", pivotq1)