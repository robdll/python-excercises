import pandas as pd
df = pd.read_csv('heroes.csv', sep=';', index_col=0)

# Print a frequency table (relative frequencies, in %) of Intelligence, sorted by frequency descending
print(df['Intelligence'].value_counts() / df['Intelligence'].value_counts().sum())
print(df['Intelligence'].value_counts(normalize=True)) 
# Print the publisher with the most heroes with high intelligence
print(df[df['Intelligence'] == 'high'].groupby('Publisher')['Intelligence'].count().idxmax())
# Print the average height of heroes grouped by Intelligence level, sorted from tallest to shortest
print()
print(df.groupby('Intelligence')['Height'].mean().sort_values(ascending=False))