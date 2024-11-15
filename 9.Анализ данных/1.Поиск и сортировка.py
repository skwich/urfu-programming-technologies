import pandas as pd

vacancies = pd.read_csv('vacancies_small.csv')

column = input()
key = input()
sort_by = input()
sort_type = True if input() == 'asc' else False
vacancies.index.name = 'IND'
output = (vacancies
    [vacancies[column].isin([key,key.lower(),key.upper()])]
    .sort_values(by=[sort_by, 'IND'], ascending=[sort_type, True])['name']
    .tolist()
)
print(output)