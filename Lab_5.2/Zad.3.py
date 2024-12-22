import pandas as pd

df = pd.read_csv(
    'demografia.csv',
    decimal=',',
    na_values=['n/a', 'NA', '-' ])

max_ze_wszystkich_lat = df.drop(columns=['KRAJE']).max().max()

max_rok = df.drop(columns=['KRAJE']).max().idxmax()

max_przyrost_kraj = df.loc[df[max_rok].idxmax(), 'KRAJE']

print(f'Największy przyrost to: {max_ze_wszystkich_lat}. Był on w roku {max_rok}. Ten przyrost dotyczy kraju {max_przyrost_kraj}')
