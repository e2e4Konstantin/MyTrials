
#you can delete column on i index like this:

df.drop(df.columns[i], axis=1)

cols = [1,2,4,5,12]
df_after_dropping = df.drop(df.columns[cols],axis=1)


df.drop(df.columns[[2,3,5]], axis = 1)

column_numbers = [x for x in range(df.shape[1])]  # list of columns' integer indices

column_numbers .remove(0) #removing column integer index 0
df.iloc[:, column_numbers] #return all columns except the 0th column



df=df[~df.Page.str.contains('\?')]

df = df.drop(df[df.score < 50].index)
df = df.drop(df[(df.score < 50) & (df.score > 20)].index)
df[df['column name'].map(len) < 2]

df[df['column name'].map(lambda x: str(x)!=".")]

# faster
df = df[df.score > 50]

# Say you want to delete all rows with negative values. One liner solution is:-

df = df[(df > 0).all(axis=1)]

# This can easily be extended to filter out rows containing NaN s (non numeric entries):-

df = df[(~df.isnull()).all(axis=1)]

# This can also be simplified for cases like: Delete all rows where column E is negative

df = df[(df.E>0)]

# In pandas you can do str.len with your boundary and using the Boolean result to filter it .

df[df['column name'].str.len().lt(2)]


# Let us assume that you want to drop the column with 'header' so get that column in a list first.

text_data = df['name'].tolist()

#now apply some function on the every element of the list and put that in a panda series:

text_length = pd.Series([func(t) for t in text_data])

# in my case I was just trying to get the number of tokens:

text_length = pd.Series([len(t.split()) for t in text_data])

#now add one extra column with the above series in the data frame:

df = df.assign(text_length = text_length .values)

# now we can apply condition on the new column such as:

df = df[df.text_length  >  10]

def pass_filter(df, label, length, pass_type):
    text_data = df[label].tolist()
    text_length = pd.Series([len(t.split()) for t in text_data])
    df = df.assign(text_length = text_length .values)
    if pass_type == 'high':
        df = df[df.text_length  >  length]
     if pass_type == 'low':
        df = df[df.text_length  <  length]
     df = df.drop(columns=['text_length'])
     return df