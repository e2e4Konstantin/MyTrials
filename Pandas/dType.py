import pandas as pd
import numpy as np
from pandas import Series, DataFrame

s = Series([10, 20, 30, 40, 50, 60])
print(s)
print(s.dtype)
print(s.values)
print(type(s.values))

s[2] = 15987
print(s.values)

s[2] = 15.987
print(s.values)
print(s.dtype)

s[2] = np.nan
print(s)
print(s.dtype)

s = Series([10, 20, 30, 40, 50, 60], dtype=pd.Int32Dtype())
print(s)
s[2] = np.nan
print(s)
print(pd.NA)


df = DataFrame(
    {
        'a': [10, 20, 30, 40, 50, 60],
        'b': [1.1, 2.2, 3.30, 4.40, 5.50, 6.60],
        'c': "hello my darling and my hut".split()
    }
)
print(df)
print(df.dtypes)
df = df.convert_dtypes()
print(df)
print(df.dtypes)
df.loc[2, 'c'] = pd.NA
print(df)
print(df.dtypes)





