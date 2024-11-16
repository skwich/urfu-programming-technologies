import pandas as pd

vacancies = pd.read_csv('vacancies_small.csv')

df = vacancies[['area_name', 'salary_from', 'salary_to', 'salary_currency']]
df = df.loc[df['salary_currency'] == 'RUR']

df['average_salary'] = df[['salary_from','salary_to']].mean(1, skipna=True)

df = df.drop(['salary_from', 'salary_to', 'salary_currency'], axis=1)

dictionary = (df
              .groupby('area_name')['average_salary']
              .agg('mean')
              .round()
              .astype(int)
              .to_dict()
)

print(dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True)))