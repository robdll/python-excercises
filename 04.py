import pandas as pd
df = pd.read_csv('heroes.csv', sep=';', index_col=0)

# Print how many heroes have missing values in the Height column
unheight_heroes = df['Height'].isnull().sum()
print(unheight_heroes)
# Print the top 5 tallest heroes (name + height)
tallest = df['Height'].sort_values(ascending=False).head()
print(tallest)
# Print the number of heroes per Publisher (hint: you know this one from the cheatsheets!)
print(df['Publisher'].value_counts())