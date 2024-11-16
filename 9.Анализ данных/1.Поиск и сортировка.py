import pandas as pd

vacancies = pd.read_csv('vacancies_small.csv')

column = input()
key = input()
sort_by = input()
sort_type = True if input() == 'asc' else False

vacancies.index.name = 'IND'
print(
    vacancies
    [vacancies[column].str.contains(key, case=False, na=False)]
    .sort_values(by=[sort_by, 'IND'], ascending=[sort_type, True])['name']
    .tolist()
)