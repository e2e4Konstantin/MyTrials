import pandas as pd
import numpy as np
from pandas import DataFrame



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





