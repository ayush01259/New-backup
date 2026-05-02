import pandas as pd
seires = {
    "Students":["Rohan","Rohit","Rishab","Raumit","Robin"],
    "Marks":[45,67,89,56,72]
}
df = pd.DataFrame(seires)
print(df["Marks"])
print(df)
print("Mark of 2nd student:\n",df["Marks"][1])
print("Mean of all marks:\n",df["Marks"].mean())


# a little reminder to do the same in series 
marks = pd.Series([45,67,89,56,72], index=["Rohan","Rohit","Robin","Rishabh","Raumit"])
print(marks)
print("2nd students ke marks:\n", marks.iloc[1])
print("Mean of all marks:\n", marks.mean())