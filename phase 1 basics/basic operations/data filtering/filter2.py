import pandas as pd

data = {
    "OrderID": [101,102,103,104,105,106,107,108,109,110],
    "Product": ["Laptop","Shirt","Rice","Mobile","Shoes","Headphones","Sugar","T-shirt","Keyboard","Jeans"],
    "Category": ["Electronics","Clothing","Grocery","Electronics","Clothing","Electronics","Grocery","Clothing","Electronics","Clothing"],
    "Price": [50000,1200,50,15000,2500,2000,45,800,1500,2000],
    "Quantity": [1,2,20,1,1,3,30,4,2,1],
    "Region": ["North","South","East","West","North","South","West","East","North","West"],
    "Salesperson": ["Ravi","Neha","Amit","Simran","Ravi","Priya","Arjun","Ravi","Neha","Simran"]
}

df = pd.DataFrame(data)
df["Total"] = df["Price"] * df["Quantity"]  # auto calculate

print(df)
print(df[df["Category"]=="Electronics"])

# printing where price > 5000
print("Price over 5000", df[df["Price"]> 5000])

# printing where region = north and quantity over 1 
print("Region and quantity based filtering :\n", df[(df["Region"]=="North") & (df["Quantity"]>1)])

# products whose total > 10000
print("Total over 10000:\n", df[df["Total"]>10000])

# Records of salesperson ravi
print("Salesperson Ravi :\n", df[df["Salesperson"] == "Ravi"])

# Category = clothing and price is less than 2000
print("Cloths under 2000\n", df[(df["Category"] == "Clothing") & (df["Price"]< 2000)])


# to filter with starting alphabet of the name
print("Products starting with S :\n", df[df["Product"].str.startswith("S")])

# to filter with ending alphabet of the name
print("Ending cahracter S:\n", df[df["Product"].str.endswith("s")])

# products containg top
print("Proucts contianing top:\n", df[df["Product"].str.contains("top")])
