import math
import pandas as pd
import sqlite3

df_currency = pd.read_csv('valutes.csv', index_col='date')
csv_merged = pd.read_csv('vacancies_dif_currencies.csv')
result = pd.DataFrame(columns=['id','name','salary','area_name','published_at'])

def to_rub(df):
    salary, currency, date = df["salary"], df["salary_currency"], df["published_at"][:7]
    if currency == "RUR":
        return salary
    if salary > 0 and currency is not None and any(df_currency.index.isin([date])):
        value = df_currency[df_currency.index == date][currency].values[0]
        if value > 0:
            return salary * value
    return None

csv_merged['salary'] = csv_merged[['salary_from','salary_to']].mean(axis=1)
csv_merged['salary'] = csv_merged.apply(to_rub, axis=1)
result['name'] = csv_merged['name']
result['salary'] = csv_merged['salary']
result['area_name'] = csv_merged['area_name']
result['published_at'] = csv_merged['published_at']
result.dropna(inplace=True)

conn = sqlite3.connect('student_works/vacancies.db')
result.to_sql('vacancies', conn, index=False)
conn.close()