import pandas as pd
df = pd.DataFrame([["30-12-2010", 40.7],
                  ["31-12-2010", 40.5]],
                  columns = ["Date","Temp"],
                  index = ['Seattle', 'Sanfrancesco']
                  )
print(df)
print("Stacked DataFrame:\n", df.stack())

print()

multi_col1 = pd.MultiIndex.from_tuples(
    [('Temp', 'Min'), ('Wind', 'Mph')])
df = pd.DataFrame(
    [[38.6, 8], [40.2, 6]],
    index =  ['Seattle', 'Sanfrancesco'],
    columns=multi_col1
)
print(df)
print("Stacked DataFrame:\n", df.stack())