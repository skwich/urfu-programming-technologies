from prettytable import PrettyTable, ALL
import csv
import re

#декоратор получения списка вакансий
def get_vacancies(func):
    def wrapper(*args):
        vacancies_list, titles, filter_name, filter_text = func(*args)
        vacancies = []
        for row in vacancies_list:
            gen = {key:value for (key,value) in zip(titles, row)}
            vacancies.append(gen)
        return vacancies, filter_name, filter_text
    return wrapper

#декоратор для применение фильтра к вакансиям
def apply_filter(func):
    def wrapper(*args):
        vacancies, filter_name, filter_text = func(*args)

        if filter_name == '' or filter_text == '':
            return vacancies

        new_vacancies_list = []
        for vacancy in vacancies:
            if filter_name == "Оклад":
                salary = re.findall(r'\d+ \d+', vacancy[filter_name])
                if len(salary):
                    salary_from, salary_to = (lambda x: (x[0].replace(' ', ''),x[1].replace(' ', '')))(salary)
                    if int(salary_from) <= int(filter_text) and int(filter_text) <= int(salary_to):
                        new_vacancies_list.append(vacancy)
            elif filter_name == "Идентификатор валюты оклада":
                currency = re.findall(r'[^()]+', vacancy["Оклад"])[1]
                if currency == filter_text:
                    new_vacancies_list.append(vacancy)
            else:
                if filter_text in vacancy[filter_name]:
                    new_vacancies_list.append(vacancy)
        return new_vacancies_list
    return wrapper

#декоратор для форматирования текста вакансий
def apply_format_to_text(func):
    def wrapper(*args):
        vacancies = func(*args)
        for vacancy in vacancies:
            for (key, value) in vacancy.items():
                vacancy[key] = value if len(value) <= 100 else value[:100] + "..."
        return vacancies
    return wrapper

@apply_format_to_text
@apply_filter
@get_vacancies
def csv_reader(file_name, filter_name, filter_text):
    with open(file_name, encoding='utf_8_sig') as csv_file:
        reader = csv.reader(csv_file)
        titles = next(reader)
        return list(reader), titles, filter_name, filter_text

#декоратор для форматирования таблицы
def apply_format_to_table(func):
    def wrapper(*args):
        table, vacancies, from_to, titles = func(*args)
        table.field_names = ['№'] + list(vacancies[0].keys())
        table.max_width = 20
        table.hrules = ALL
        table.align = 'l'
        return table, vacancies, from_to, titles
    return wrapper

#декоратор для заполнения таблицы данными
def fill_table(func):
    def wrapper(*args):
        table, vacancies, from_to, titles = func(*args)    
        for i, vacancy in enumerate(vacancies, 1):
            table.add_row([i] + list(vacancy.values()))
        table = table.get_string(start=from_to[0], end=from_to[1],
                             fields=['№'] + titles.split(', ') if titles != '' else table.field_names)
        return table
    return wrapper

@fill_table
@apply_format_to_table
def create_table(vacancies, from_to, titles):
    table = PrettyTable()
    return table, vacancies, from_to, titles

def get_range(input, max):
    match len(input):
        case 0:
            return [0, max + 1]
        case 1:
            return [input[0] - 1, max]
        case 2:
            return [input[0] - 1, input[1]]

def main():
    file_name = input()

    filter_str = input()
    filter_name, filter_text = list(map(str, filter_str.split(': '))) if filter_str != '' else ('', '')
    vacancies = csv_reader(file_name, filter_name, filter_text)

    input_range = input().split()
    from_to = get_range(list(map(int, input_range)), len(vacancies))

    titles = input()

    table = create_table(vacancies, from_to, titles)
    print(table)

if __name__ == '__main__':
    main()