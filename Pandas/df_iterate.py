import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3], 'B': ['apple', 'banana', 'cherry']}
df = pd.DataFrame(data)
print(df)
print('---')
# Iterate over rows in the DataFrame
for index, row in df.iterrows():
    print(f'Row index: {index} Values in row: {row}')
    
    print('---')


for index, row in df.iterrows():
    for column in df.columns:
        cell_value = row[column]
        print(f'Cell value at row {index} and column {column}: {cell_value}')    