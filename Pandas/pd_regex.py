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

ind = df.Industry.tolist()
print(len(ind))
uind = []
for i in ind:
    if 'consumer' in i.lower():
        uind.append(i)

print(len(uind))
print(uind)

print(df.loc[df['Industry'].str.contains('Consume')])
print(df.loc[~df['Industry'].str.contains('Consume')])

print(df.loc[(df['Industry'].str.contains('Consume')) | (df['Industry'].str.lower().str.contains('transportation'))])

print(df.loc[(df['Industry'].str.contains('consume|transportation', case=False, regex=True))])

