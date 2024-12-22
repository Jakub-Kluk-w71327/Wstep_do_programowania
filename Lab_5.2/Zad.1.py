import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv(
    'demografia.csv',
    decimal=',',
    na_values=['n/a', 'NA', '-' ])

print(df)
