import pandas as pd

data = {
    "Salesperson": ["Ravi", "Neha", "Amit", "Ravi", "Amit", "Neha", "Simran", "Simran"],
    "Region": ["North", "South", "East", "North", "West", "South", "West", "East"],
    "Product": ["Laptop", "Shoes", "Laptop", "Phone", "Shoes", "Phone", "Phone", "Laptop"],
    "Sales": [50000, 1200, 45000, 18000, 2500, 22000, 19000, 52000],
    "Quantity": [1, 3, 2, 1, 4, 2, 1, 3]
}

df = pd.DataFrame(data)

# total sales per region 
total_sales_region = df.pivot_table(values="Sales", index="Region", aggfunc="sum")
print("Total sales on the basis of region : \n", total_sales_region)


# sales per region per product
sales_per_region_product = df.pivot_table(values="Sales", index="Region", columns="Product", aggfunc="sum")
print("Sales per region per prduct : \n", sales_per_region_product)

# total quantity per salesperson 
quantity_per_person = df.pivot_table(values="Quantity", index="Salesperson", aggfunc="sum")
print("Total quantity per salesperson :\n", quantity_per_person)

# mutli aggregation pivot tales ( sales + quantity )
multi_agg = df.pivot_table(values=["Sales", "Quantity"], index="Region", aggfunc={"Sales":"sum", "Quantity":"mean"} )
print("Multi aggregation {sales and quantity} :\n", multi_agg)


# filling missing values
missing_fill = sales_per_region_product.fillna(0)
print("Filling missing data of sales per region product function : \n", missing_fill)

# adding subtotals / margins 
pivot_margin = df.pivot_table(values="Sales", index="Region", columns="Product", aggfunc="sum", margins=True)
print("\n \nadding a row named margin : \n",pivot_margin)


# crosstab 

cross = pd.crosstab(df["Region"], df["Product"])
print(cross)