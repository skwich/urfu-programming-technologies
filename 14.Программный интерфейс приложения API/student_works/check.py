import pandas as pd

df1 = pd.read_csv('currency.csv')

df2 = pd.read_csv('correct_result.csv')

if df1.equals(df2):
    print("Содержимое файлов идентично.")
else:
    print("Содержимое файлов различается.")