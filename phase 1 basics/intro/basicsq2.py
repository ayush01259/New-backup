import pandas as pd
data = {
    "Name":["Aman","Ravi","Neha","Priya"],
    "Age":[15,16,14,15],
    "Grade":["B","A","C","A"]
}

df = pd.DataFrame(data)
print("Full dataframe:\n", df)
print("Only name and grade columnns:\n", df[["Name", "Grade"]])
print("No of rows and columns:\n", df.shape)