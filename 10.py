import pandas as pd
df = pd.read_csv('heroes.csv', sep=';', index_col=0)


# Create a new column is_heavy that is True if the hero's weight is above the average weight, False otherwise
avg_weight = df['Weight'].mean()
df['is_heavy'] = df['Weight'] > avg_weight

print(df['is_heavy'])
# Print how many heroes are heavy vs not heavy
print(df['is_heavy'].value_counts())

#Print the percentage of heavy heroes for each Gender
print(df.groupby('Gender')['is_heavy'].value_counts(normalize=True))


