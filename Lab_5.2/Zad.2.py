import pandas as pd

df = pd.read_csv(
    'demografia.csv',
    decimal=',',
    na_values=['n/a', 'NA', '-' ])

max_przyrost_index = df['2022'].idxmax()
kraj_max_przyrost = df.loc[max_przyrost_index, 'KRAJE'] #wybór wiersza na podstawie etykiety

print(f'Kraj w którym odnotowano największy przyrost ludności w roku 2022 to: {kraj_max_przyrost} ')