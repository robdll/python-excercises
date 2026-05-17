
import pandas as pd

df = pd.read_csv('heroes.csv', sep=';', index_col=0)

# Compute and print the Gini heterogeneity index for the Eye color column 
eye_mod_counts = df['Eye color'].value_counts() # occurencies by type
freq_eye_mod = eye_mod_counts / eye_mod_counts.sum() # frequency = occurence / tot_occurences
print(freq_eye_mod.sum())
gini = 1 - (freq_eye_mod ** 2).sum()
print(f'Gini: {gini:.4f}')

# Print the correlation between Height and Weight

def covariazione(s1, s2, frameWithNull):
  frame = frameWithNull[[s1, s2]].dropna()
  N = len(clean_frame)
  s1_bar = frame[s1].sum() / len(frame[s1])
  s2_bar = frame[s2].sum() / len(frame[s2])
  scarto_1 = frame[s1] - s1_bar
  scarto_2 = frame[s2] - s2_bar
  scarti_prodotto = scarto_1 * scarto_2
  return scarti_prodotto.sum() / (N -1)

std_height = df['Height'].std()
std_weight = df['Weight'].std()
correlazione = covariazione('Height', 'Weight', df) / (std_height * std_weight)
print(correlazione)

# Print a frequency table (relative frequencies) of Alignment sorted by frequency descending
print(df['Alignment'].unique())
