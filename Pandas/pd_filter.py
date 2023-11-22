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

print(df.filter(['Name', 'Country', 'Number of employees']))
print(df.filter(['Name', 'Country', 'Number of employees']).Name.str.contains('group', case=False))
print(df.filter(['Name', 'Country', 'Number of employees']).Name.str.contains('group', case=False).value_counts())
print(df[df.filter(['Name', 'Country', 'Number of employees']).Name.str.contains('group', case=False) == True])
print(df[df.filter(['Name', 'Country', 'Number of employees']).Name.str.contains('group', case=False)])
print(df[df.Name.str.contains('group', case=False)].filter(['Name', 'Country', 'Number of employees']))


df.rename(columns={"Number of employees": "employees"},  inplace=True)
print(df)
print(df.query('employees > 9000'))
