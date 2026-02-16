import pandas as pd
from collections import Counter

vacancies = pd.read_csv('vacancies_small.csv')

name = input()
sort_type = False if input() == 'asc' else True


def format_cell(x):
    if isinstance(x, str):
        return x.split('\n')

df = vacancies[vacancies['name'].str.contains(name, case=False, na=False)]
skills = df[df['key_skills'].notna()]
skills = skills['key_skills'].apply(lambda x: format_cell(x)).tolist()
counter = Counter(sum(skills, []))
print(sorted(counter.most_common(5), key=lambda x: x[1], reverse=sort_type))