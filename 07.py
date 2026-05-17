import pandas as pd

df = pd.read_csv('heroes.csv', sep=';', index_col=0)
df['BMI'] = df['Weight'] / (df['Height']/100)**2


# Print the mean, std and median of Height for each Gender (use groupby)
gender_mean_std_median = df.groupby('Gender')['Height'].agg(['mean', 'std', 'median'])
print(gender_mean_std_median)

# Alternative solution
#gender_mean = df.groupby('Gender')['Height'].mean()
#gender_std = df.groupby('Gender')['Height'].std()
#gender_median = df.groupby('Gender')['Height'].median()
#print(f'gender_mean: {gender_mean}')
#print(f'gender_std: {gender_std}')
#print(f'gender_median: {gender_median}')

#Print how many heroes have both Height and Weight missing (both at the same time)
misterious = df[ df['Height'].isnull() & df['Weight'].isnull()]
print(f'misterious: {len(misterious)}')

#Find the Publisher with the highest average Strength (one line!)
highest_avg = df.groupby('Publisher')['Strength'].mean().idxmax()
print(f'highest_avg: {highest_avg}')

# Alternatie solution
#highest_avg = df.groupby('Publisher')['Strength'].mean().sort_values(ascending=False).head(1)
#print(f'highest_avg: {highest_avg}')

