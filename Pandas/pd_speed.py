import pandas as pd
import numpy as np
# pip install parquet, fastparquet


# size = 1000

def set_df(size):
    df = pd.DataFrame()
    df['position'] = np.random.choice(['left', 'middle', 'right'], size)
    df['age'] = np.random.randint(1, 50, size)
    df['team'] = np.random.choice(['yellow', 'red', 'green', 'blue'], size)
    df['win'] = np.random.choice(['yes', 'no'], size)
    df['prob'] = np.random.uniform(0, 1, size)
    return df

def set_dtype(df):
    df['position'] = df['position'].astype('category')
    df['team'] = df['team'].astype('category')
    df['age'] = df['age'].astype('int8')
    df['prob'] = df['prob'].astype('float32')
    df['win'] = df['win'].map({'yes': True, 'no': False})

d = set_df(1_000_000)

print(d.head(3))
print(d.shape)
print(d.info(memory_usage=True))
# print(d.memory_usage())
d['rank_age'] = d.groupby(['team', 'position']).age.rank()
d['rank_prob'] = d.groupby(['team', 'position']).prob.rank()
print(d.head(3))
print(d.info(memory_usage=True))
set_dtype(d)
print(d.info(memory_usage=True))
print(d.head(3))

d.to_csv('tmp.csv', index=False)
d = pd.read_csv('tmp.csv')
print(d.head())
print(d.info(memory_usage=True))

d.to_pickle('tmp.pickle')
d = pd.read_pickle('tmp.pickle')
print(d.head())
print(d.info(memory_usage=True))
set_dtype(d)
print(d.info(memory_usage=True))

d.to_parquet('tmp.parquet')
d = pd.read_parquet('tmp.parquet')
print(d.head())
print(d.info(memory_usage=True))
set_dtype(d)
print(d.info(memory_usage=True))



