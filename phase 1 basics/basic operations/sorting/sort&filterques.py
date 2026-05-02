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
print("Orders from north where price is greater than 2000:\n", df[(df["Region"]=="North") & (df["Price"]> 2000)])

# sbse mehnga order as per price and product and who ordered that
most_expensive = df.nlargest(1, "Price")
print("Most expensive order:\n", most_expensive[["Product", "Price", "Salesperson"]])

# another way to do this
expensive = df.sort_values(by="Price", ascending=False).head(1)
print("Most expensive:\n", expensive[["Price", "Salesperson", "Product"]])


# question 3 : quantity 3 se jyada aur category = grocery
print("Qunatity > 3 and category = grocery\n",df[(df["Quantity"]>=3) & (df["Category"]=="Grocery")])


#sbse jyada total wala order top 1 by total
print("Most total:\n", df.nlargest(1, "Total"))

# salesperson priya ke top 2 sbse bde order
priya_total = df[df["Salesperson"]=="Priya"]
print("Priyas top 2 order:\n", priya_total.nlargest(2, "Total"))