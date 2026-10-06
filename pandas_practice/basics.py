import pandas as pd

# Series: 1d labelled data
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)

# DataFrame: 2d table
df = pd.DataFrame({
    'name': ['asha', 'bala', 'chen', 'dev', 'esha', 'faiz'],
    'age': [19, 21, 20, 22, 19, 20],
    'marks': [35, 62, 48, 91, 77, None],
})
print(df.shape, list(df.columns))
print(df.dtypes)
print(df.head(3))
print(df.describe())

# selection: iloc uses positions, loc uses labels
print(df.iloc[0:2])                    # rows at positions 0,1
print(df.loc[0:2, ['name', 'marks']])  # labels 0..2 inclusive
print(df[df['marks'] > 50])            # filter rows

# cleaning
print(df.isnull().sum())
df['marks'] = df['marks'].fillna(df['marks'].mean())

# add, rename, drop columns
df['status'] = ['pass' if m > 40 else 'fail' for m in df['marks']]
df = df.rename(columns={'name': 'NAME'})
df = df.drop('age', axis=1)  # axis=1 is columns, axis=0 is rows
print(df)
print(df.groupby('status')['marks'].mean())
