import pandas as pd
import numpy as np

print(pd.__version__)
#
df = pd.read_csv('test_data.csv')
print(df)

df.drop("cats", axis='columns', inplace=True)
df.drop(7, axis='index', inplace=True)
# df.to_csv('data.csv', index=False)


print(df.info(verbose=False, memory_usage=True, show_counts=True))
# print(df.head(5))
# print(df.tail(5))
print(df.shape)
print(df.index)
print(df.columns)
print(df)
print(df.dtypes)
df['price'].astype('float64')
df['name'].astype(str)
df['state'].astype("string")
print(df.dtypes)
print()
#
print(df['name'].str.strip())
print(df[df['name'].str.strip() == 'Dave'])
df['name'] = df['name'].str.strip()
print(df)
print(df.dtypes.to_dict())
print(df.columns)

for column in df.columns:
    print(df[column].dtype)
    if df[column].dtype != np.float64 and df[column].dtype != np.int64:
        df[column] = df[column].str.strip()
print(df)
# !!!
print(df.state.str.match("CA"))
print(df.columns.str.strip())
print(df['name'].value_counts(dropna=False))

print(df.dropna(subset=["name"], inplace=True))
print(df)

print(df['name'].str[:3])
print(df[df['name'].str.lower().str.contains("l")])
print()
print(df[df['name'].str.lower().str.startswith("a")])
print(df['name'].str.lower().str.split(" "))




print(df.loc[:, ["state", "price"]].groupby("state", as_index=False).sum())
#
print(df.loc[:, ["state", "price"]].groupby("state", as_index=False).agg({"state": "count"}).sort_values('state', ascending=False))
print(df.groupby("state", as_index=False).agg({"name": "count"}).sort_values('name', ascending=False))
print(df.groupby("state", as_index=False).agg({"name": "count"}).sort_values('name', ascending=False).shape)


print(df[df['name'].notna()])
print(df[df['name'].notna()].groupby("state").agg({"name": pd.Series.nunique}))
print()
print(df[df['name'].notna()].groupby("state").agg({"name": pd.Series.nunique}).name.sum())
# print(df[df['price']>0])

# print(df.query('price > 50'))
print(df.query("state == 'NY' & name.notna()"))


df[['first_name', 'middle_name', 'last_name']] = df['name'].str.split(pat=' ', expand=True)





