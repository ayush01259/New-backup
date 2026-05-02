import pandas as pd
data = {
    "Salesperson": ["Ravi", "Neha", "Amit", "Ravi", "Amit", "Neha", "Simran", "Simran"],
    "Region": ["North", "South", "East", "North", "West", "South", "West", "East"],
    "Product": ["Laptop", "Shoes", "Laptop", "Phone", "Shoes", "Phone", "Phone", "Laptop"],
    "Sales": [50000, 1200, 45000, 18000, 2500, 22000, 19000, 52000],
    "Quantity": [1, 3, 2, 1, 4, 2, 1, 3]
}
df = pd.DataFrame(data)
# q1: summary table for the following : total sales, average sales , maximum quantity, total quantity sold

summary = df.groupby("Product").agg({
        "Sales" : ["sum", "mean"], 
        "Quantity": ["max", "sum"]
}).round(2)
print(summary)

# q2 Most sales in the region by the salesperson
grouped = df.groupby(["Region",  "Salesperson"])["Sales"].sum()
top_sales_by_region = grouped.groupby(level=0).idxmax()
print("\n \n",top_sales_by_region)

#q3 product wise summary for every region 
product_summary = df.groupby(["Region", "Product"]).agg(
   Total_sales = ("Sales", "sum"),
   Total_Quantity = ("Quantity", "sum"), 
   Avg_Sales = ("Sales", "mean")
)
print(product_summary)

# q4 identifying high value customers 
high_value = df[df["Sales"]>30000].groupby("Salesperson")["Sales"].count()
print(high_value)

# q5 profit contribution for every product
margin = {"Laptop":0.15, "Phone":0.10, "Shoes":0.30, "Sugar":0.05}
df["Profit"] = df["Sales"] * df["Product"].map(margin)
print(df.groupby("Product")["Profit"].sum())


# q6 most hilarios question 
# yearly summery simulation where annual total sales, annaul total quantity, montyly average sales, annual sales revenue of every sales person would be 

df_year = pd.concat([df]* 12, ignore_index=True)
# this is to maek 12 copies to make an year

annaul_total_sales = df_year["Sales"].sum()
print(annaul_total_sales)

annaul_total_quantity = df_year["Quantity"].sum()
print(annaul_total_quantity)

monthly_average_sales = df_year["Sales"].sum()/12
print(monthly_average_sales)

annual_salesperson = df_year.groupby("Salesperson")["Sales"].sum()
print(annual_salesperson)