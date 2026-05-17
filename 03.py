import pandas as pd
df = pd.read_csv('heroes.csv', sep=';', index_col=0)

# Print the first 5 rows
print(df.head())
# Print the shape of the dataset (rows and columns)
print(df.shape)
# Print the column names
print(df.columns)


# Print the Height column
print(df['Height'])
# Print the mean, max and min height
print(df['Height'].mean())
print(df['Height'].max())
print(df['Height'].min())

# Print only the heroes taller than 200 cm (just the Height column, not the full row)
tall_heroes = df[ df['Height'] > 200]['Height']
print(tall_heroes)
