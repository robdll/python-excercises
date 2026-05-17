import pandas as pd
df = pd.read_csv('heroes.csv', sep=';', index_col=0)

# Print the average weight of female heroes vs male heroes separately
female_heroes = df[ df['Gender'] =='F']['Weight'].mean()
male_heroes = df[ df['Gender'] =='M']['Weight'].mean()
print(female_heroes)
print(male_heroes)
# Print the number of unique values in the Eye color column
eye_colors = df['Eye color'].nunique()
print(eye_colors)

# Print the hero with the highest intelligence — but careful, Intelligence is a text column 
# (low, average, good, high), so you can't use .max(). 
# Just print all unique values first and think about how to filter.

wise_values = df['Intelligence'].unique()
print(wise_values)
wiser_heroes = df[df['Intelligence'] == 'high']
print(wiser_heroes)
