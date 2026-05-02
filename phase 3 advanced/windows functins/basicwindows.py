import pandas as pd
sales = [10,20,30,40,50,60,70]
df = pd.DataFrame({"Sales": sales})

df["Rolling_mean_3"]  = df["Sales"].rolling(window=3).mean()
print("Rolling Mean  \n",df)

df["Rolling_sum_3"] = df["Sales"].rolling(window=3).sum()
print("Rolling sum  \n",df)

df["Rolling_max_3"] = df["Sales"].rolling(window=3).max()
print("Rolling Max  \n",df)





df["Expanding_mean"] = df["Sales"].expanding().mean()
print("Expanding mean \n",df)

df["Cummalative_sum"] = df["Sales"].cumsum()
print("Cumsum : \n", df)

df["cummalative_max"] = df["Sales"].cummax()
print("Cummalative max : \n", df)

df["EWM_0.3"] = df["Sales"].ewm(alpha=0.3).mean()
print("Exponential weighted moving average : \n", df)