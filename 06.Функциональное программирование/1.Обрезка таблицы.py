from prettytable import PrettyTable, ALL
import csv

def csv_reader(file_name):
    with open(file_name, encoding='utf_8_sig') as csv_file:
        reader = csv.reader(csv_file)
        titles = next(reader)
        vacancies = []
        for row in reader:
            gen = {key:value if len(value) <= 100 else value[:100] + "..." for (key,value) in zip(titles, row)}
            vacancies.append(gen)
        return vacancies

#декоратор для форматирования таблицы
def apply_format(func):
    def wrapper(*args):
        table = func(*args)
        vacancies = args[0]
        table.field_names = ['№'] + list(vacancies[0].keys())
        table.max_width = 20
        table.hrules = ALL
        table.align = 'l'
        return table
    return wrapper

#декоратор для заполнения таблицы данными
def fill_table(func):
    def wrapper(*args):
        table = func(*args)
        vacancies = args[0]
        from_to = args[1]
        titles = args[2]
        for i, vacancy in enumerate(vacancies, 1):
            table.add_row([i] + list(vacancy.values()))
        table = table.get_string(start=from_to[0], end=from_to[1],
                             fields=['№'] + titles.split(', ') if titles != '' else table.field_names)
        return table
    return wrapper

@fill_table
@apply_format
def create_table(vacancies, from_to, titles):
    table = PrettyTable()
    return table

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
    vacancies = csv_reader(file_name)
    from_to = get_range(list(map(int, input().split())), len(vacancies))
    titles = input()
    table = create_table(vacancies, from_to, titles)
    print(table)

if __name__ == '__main__':
    main()