import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3], 'B': ['apple', 'banana', 'cherry']}
df = pd.DataFrame(data)

# Iterate over cells in the DataFrame
for column, series in df.iteritems():
    for index, value in series.items():
        print(f'Column: {column}, Index: {index}, Value: {value}')