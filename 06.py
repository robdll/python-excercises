import pandas as pd
df = pd.read_csv('heroes.csv', sep=';', index_col=0)

# Compute the BMI for each hero (Weight / (Height/100)²) and add it as a new column called BMI
weights = df['Weight']
heights_percent = df['Height'] / 100
df['bmi'] = weights / (heights_percent ** 2)
# Print the top 3 heroes with the highest BMI (name + BMI only)
top_bmi = df['bmi'].sort_values(ascending=False)
print(top_bmi[:3])

# Print the average BMI for each Publisher (hint: think groupby — or use what you already know!)
avg_bmi_of = df.groupby(by='Publisher')['bmi'].mean()
# avg_bmi_of = df.dropna(subset=['bmi']).groupby('Publisher')['bmi'].mean() # Drop NaN
print(avg_bmi_of)

