import pandas as pd
data ={
    "Name": ["Aman", "Ravi", "Neha", "Priya"],
    "Age": [15, 16, 14, 15],
    "Grade": ["B", "A", "C", "A"]
}

df = pd.DataFrame(data)
df["Marks"] = [58, 93, 91,99]
print("Before adding :\n", df)
df.loc[4] = ["Arjun", 19, "C", 78]
print(df)
# if there is data where we dont know the index and have to add so we can use this
# df.loc[len(df)] 

# adding some rows with modern pandas style 
new_row = pd.DataFrame([{
    "Name":"Ayush", 
    "Age":19, 
    "Grade": "A"
}])
df = pd.concat([df, new_row], ignore_index=True)
print("DF with modern pandas adding:\n", df)

# removing rows
df = df.drop(2, axis=0)
print(df)