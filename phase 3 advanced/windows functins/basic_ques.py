import pandas as pd
Sales = [10,20,30,40,50,60]
df = pd.DataFrame({"Sales" : Sales})
print(df)

df["rollingmedian"] = df["Sales"].rolling(window=3).median()
print("Median of 3 day rolling : \n", df)

df["rollingmin"] = df["Sales"].rolling(window=4).min()
print("4 day rolling min : \n", df)
 
df["exapndingsum"] = df["Sales"].expanding().sum()
print("Expanding sum : \n", df)

df["Cummalative_product"] = df["Sales"].cumprod()
print("Sales ka cummalative product : \n", df)

df["exponential_moving_average"] = df["Sales"].ewm(alpha=0.5).mean()
print("2 window ke sath exponential moving average :  \n", df)
# alpha ke value decide krne ke lie jitne windows honge usse 1 se divide kr do 


# new ema = alpha * current value + ( 1 - alpha ) * previous value 
