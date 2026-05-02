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
df.sort_values(by="Price")   # Price ke hisaab se ascending sort
df.sort_values(by="Price", ascending=False)  # descending sort
print(df.sort_values(by="Price"))  # Price ke hisaab se ascending sort
print("\n\n",df.sort_values(by="Price", ascending=False))

# if more than one sorting column
print("2 column sorted:\n", df.sort_values(by=["Category", "Price"], ascending=[True, False]))

# sorting top N rows
print("Top 3 rows by price\n", df.sort_values(by="Price", ascending=False).head(3) )

# top 3 largest products 
print("Top 3 products with most price:\n", df.nlargest(3, "Price"))

# top 3 products with lowest price
print("Top 3 products with lowest price:\n", df.nsmallest(3, "Price"))

# top 3 most ordered total 
print("Top 3 total:\n", df.nlargest(3, "Total"))

# lowest 2 price 
print("Lowest 2 price items:\n", df.nsmallest(2, "Price"))