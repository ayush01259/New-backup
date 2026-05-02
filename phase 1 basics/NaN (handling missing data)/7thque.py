import pandas as pd
import numpy as np

np.random.seed(0)
# isse random datasheet generate krne pr bar bar same data aata h

data = {
    'A' : np.random.randint(1,20, size=10),
    'B' : np.random.randint(1,20, size=10)
}

df = pd.DataFrame(data)

# randomly inserting NaN in dataframe by 25%
for col in df.columns:
    df.loc[df.sample(frac=0.25).index, col] = np.nan

print("Original dataframe with NaNs:\n", df)


# filling dataframe by ffill (forward fill)

# df_ffill = df.fillna(method='ffill')

# this is now deprecated so its now can be used as
df_ffill = df.ffill()

print("\nDataframe after Forward fill:\n", df_ffill)

# filling dataframe with bfill (backward fill)
# df_bfill = df.fillna(method='bfill')

# here too this could be like this
df_bfill = df.bfill()

print("\nDataframe after backward fill :\n", df_bfill)