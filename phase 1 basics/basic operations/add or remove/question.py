import pandas as pd
data = {
    "Name" : ["Aman", "Ayush", "Anuj", "Ankush"],
    "Age" : [19,19, 18,17],
    "State":["Bihar","Bihar","Bihar","Bihar"]
}
df = pd.DataFrame(data)
print(df)
# adding a column named city
df["City"] = ["Nawada", "Nawada", "Nawada", "Nawada"]

# deleting 1st index row
df = df.drop(1, axis=0)

# adding new row 
df.loc[4] = ["Khushi", 21, "Bihar", "Nawada"]
print(df)