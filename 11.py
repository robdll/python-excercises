import pandas as pd
df = pd.read_csv('heroes.csv', sep=';', index_col=0)

def calc_iqr(s1, frame):
  q1 = frame[s1].quantile(.25)
  q3 = frame[s1].quantile(.75)
  iqr = q3 - q1
  return [q1, q3, iqr]

def get_outlier (q1, q3, iqr, s1, frame):
  low_threeshold = q1 - (1.5 * iqr)
  high_threeshold = q3 + (1.5 * iqr)
  below_outlier = frame[frame[s1] < low_threeshold]
  above_outlier = frame[frame[s1] > high_threeshold]
  return pd.concat([below_outlier, above_outlier])

# Compute the IQR of Strength
q1_s, q3_s, iqr_s = calc_iqr('Strength', df)
print(f'Strength q1: {q1_s}, q3: {q3_s}, IQR: {iqr_s}')

#Find all heroes that are outliers in Strength 
#(using the box plot rule: below Q1-1.5·IQR or above Q3+1.5·IQR)
print(get_outlier(q1_s, q3_s, iqr_s, 'Strength', df))

q1_w, q3_w, iqr_w = calc_iqr('Weight', df)
print(f'Weight q1: {q1_w}, q3: {q3_w}, IQR: {iqr_w}')
print(get_outlier(q1_w, q3_w, iqr_w, 'Weight', df)['Weight'])


