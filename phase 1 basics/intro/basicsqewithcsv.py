import pandas as pd
data = pd.read_csv("./PANDAS/phase 1 basics/intro/students_data.csv")
top_students = data.sort_values(by="Marks", ascending=False).head(3)
print("Top 3 studnets with highest marks :\n", top_students)

# average marks of male vs female
avg_marks = data.groupby("Gender")["Marks"].mean()
print(avg_marks)


# counting grade 
count_grade= data.groupby("Grade")["Grade"].count()
print(count_grade)
# tips for me in this 
# 1st tipp (to do this in more cleaner way)
print(data["Grade"].value_counts())

# tip 2 ( a powerful variation to do this)
print(data.groupby("Grade")["Marks"].agg(["count", "mean", "max", "min"]))


# eldest and youngest child
