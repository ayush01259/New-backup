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
print("Top 3 most expensive products:\n", df.nlargest(3, "Price"))
# also by sort_values
print("Top 3 most expensive products by sort_values method:\n", df.sort_values(by="Price", ascending=False).head(3))


# lowest 2 quantity wale orders 
print("Lowest two orders:\n", df.nsmallest(2, "Quantity"))
# by sort_values
print("Lowest two orders by sort_values:\n", df.sort_values(by="Quantity").head(2))

# most total in every category  doing by sort_values
print("Biggest total of products in every category:\n",df.loc[df.groupby("Category")["Total"].idxmax()])