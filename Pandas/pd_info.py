import pandas as pd
from pandas import Series, DataFrame
import numpy as np

df = DataFrame(np.random.randint(0, 1000, [6, 6]), index=list('abcdef'), columns=list('UVWXYZ'))

print(f"{df.info(verbose=False, memory_usage='deep', show_counts=True)}")
print(f"использовано памяти: {df.memory_usage(index=True, deep=True).sum():_} bytes")
print(f"размерность: {df.shape}")
print(f"индексы: {df.index}")
print(f"названия столбцов: {type(df.columns)} {list(df.columns)}")
print(f"типы данных столбцов: '{df.dtypes.values.tolist()}'")
print(f"{df}")
#
# print(df.columns.values.tolist().index('W'))
# print(df.columns.isin(['V', 'Y']))
# out = np.argwhere(df.columns.isin(['V', 'Y'])).ravel()
# print(out)
#
#
# print(df[df.columns[1]])
# print(f"count: {df[df.columns[1]].count()}")
# print(f"sum: {df[df.columns[1]].sum()}")
#
# print(df.columns.get_loc("W"))
# print(f"*-count: {df[df.columns[df.columns.get_loc('W')]].count()}")

# print(df['Y'] > 500)
# print(df.loc[df['Y'] > 500])
# print(df.loc[df['Y'] > 500, 'Y'])
# print(df.loc[df['Y'] > 500, 'Y'].sum())
#
# print(df.loc[:, 'Y'] > 500)
#
#
# # print(df[df.loc[:, 'Y'].notna()].count())
#
# print(df[df['Y'].notna()].filter('Y').count())

df.loc['d', 'W'] = pd.NA
df.iat[1, 2] = pd.NA
df.at['a', 'W'] = pd.NA
df.at['b', 'Z'] = ''
df.at['d', 'Z'] = pd.NA
print(df)

# print(df['Z'].notna())
# print(df['Z'].notna().value_counts())

print(df[(df['Z'].notna()) & (df['Z'] != '')].filter('Z'))

c = df[(df['Z'].notna()) & (df['Z'] != '')].filter('Z').count()
print(c.values)
print(c)

print(df['Z'].nunique(dropna=True))




# print(df[df['Z'].notna()].filter('Z'))
# print(df[df['Z'].notna()].filter('Z').count())

#
# print(df.loc[df['Z'].notna(), 'Z'])
# print(df.loc[df['Z'].notna(), 'Z'].count())
# print(type(df.loc[df['Z'].notna(), 'Z']))
# print(df.loc[df['Z'].notna(), 'Z'].value_counts())

#
# print(df[df['W'].notna()])
# print( df.loc[df['W'].notna(),'W'])
# print( df.loc[df['W'].notna(),'W'].agg(['nunique','count','size', 'sum']) )
# print(df[df['W'].notna()].W.sum())
# print(df[df['W'].notna()].W.count())
#
# print(
#     df['W'].count(), df['W'].sum(), df['W'].nunique(dropna=False), df['W'].nunique(dropna=True),
# )
# print('---')
# print(
#     df['W'].value_counts(), df.value_counts(), df.value_counts(normalize=True)
# )
#
#
#
#
#
#
#




#
#
# print(f"{[*df]}")
# df_set = {*df}
# print(f"{df_set = }")
# print(f"{*df, = }")