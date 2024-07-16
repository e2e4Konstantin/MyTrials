import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3], 'B': ['apple', 'banana', 'cherry']}
df = pd.DataFrame(data)

# Find a cell by its value
row_index, col_index = df[df == 'banana'].stack().index[0]
print(f'Cell location: ({row_index}, {col_index})')
print(f'Cell value: {df.loc[row_index, col_index]}')