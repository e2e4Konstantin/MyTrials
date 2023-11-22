import pandas as pd
import numpy as np

df = pd.read_csv('organizations.csv')
print(df.info(verbose=False, memory_usage=True, show_counts=True))
print(df.head(5))
# print(df.tail(5))
print(df.shape)
print(df.index)
print(df.columns)
print(df.dtypes)

df.drop(['Index', 'Organization Id'], axis='columns', inplace=True)
print(df.head(5))
print(df.shape)
print(df.index)
print(df.columns)

# print(df.loc[:, ['Country', 'Number of employees']].groupby("Country", as_index=False).sum())


print(len(df["Industry"].unique().tolist()))
print(df["Industry"].nunique())

print(df['Industry'].str.lower().str.split(" ", n=1).head(10))
print(df['Industry'].str.lower().str.split(" ", n=1).str.get(0).head(15))
print(df['Industry'].str.lower().str.split(" ", n=1, expand=True))

df[['first_name', 'middle_name', 'last_name']] = df['name'].str.split(pat=' ', expand=True)
df[['name', 'first_name', 'middle_name', 'last_name']]

