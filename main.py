import pandas as pd
df = pd.read_csv('qol_states_2024.csv')
print(df.head(5))
print(df.info())
print(df.describe())