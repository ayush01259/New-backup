import pandas as pd
data = {
    "OrderID":   [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    "Product":   ["Laptop", "T-Shirt", "Mobile", "Rice Bag", "Headphones", "Jeans", "Sugar", "Fan"],
    "Category":  ["Electronics", "Clothing", "Electronics", "Grocery", "Electronics", "Clothing", "Grocery", "Electronics"],
    "Price":     [55000, 700, 15000, 1200, 2500, 1200, 40, 2500],
    "Quantity":  [2, 5, 3, 4, 6, 2, 50, 3],
    "Total":     [110000, 3500, 45000, 4800, 15000, 2400, 2000, 7500],
    "Region":    ["North", "West", "South", "East", "North", "South", "East", "West"],
    "Salesperson":["Akash", "Priya", "Rohan", "Amit", "Akash", "Priya", "Amit", "Rohan"]
}
df = pd.DataFrame(data)
print(df)

# simple filtering with conditions 
electronics = df[df['Category'] == 'Electronics']
print("\nElectronics:\n\n",electronics)


# multiple filtering using more than 1 conditions
north_electronics = df[(df['Category']=='Electronics') & (df['Region'] == 'North')]
print("\nNorth electronics:\n", north_electronics)

# condition on price
expensive = df[df['Price']> 2000]
print("Products more than 2000:\n", expensive)

# or conditions
cloth_gro = df[(df['Category'] == 'Clothing') | (df['Category'] == 'Grocery')]
print("Cloths or grocery :\n", cloth_gro)

