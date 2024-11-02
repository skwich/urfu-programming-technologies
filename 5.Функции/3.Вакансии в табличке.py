from prettytable import PrettyTable
import csv

work_experience = {
    "noExperience": "Нет опыта",
    "between1And3": "От 1 года до 3 лет",
    "between3And6": "От 3 до 6 лет",
    "moreThan6": "Более 6 лет"
}

currency = {
    "AZN": "Манаты",
    "BYR": "Белорусские рубли",
    "EUR": "Евро",
    "GEL": "Грузинский лари",
    "KGS": "Киргизский сом",
    "KZT": "Тенге",
    "RUR": "Рубли",
    "UAH": "Гривны",
    "USD": "Доллары",
    "UZS": "Узбекский сум"
}

def сsv_reader(file_name):
    vacancies = []
    with open(file_name, encoding='utf_8_sig') as csv_file:
        reader = csv.reader(csv_file)
        titles = next(reader)
        for row in reader:
            vacancy = {}
            for (key,value) in zip(titles,row):
                vacancy[key] = value
            vacancies.append(vacancy)
    return vacancies

def get_salary(salary_from, salary_to, salary_gross, salary_currency):
    salary_from = f"{int(float(salary_from)):,}".replace(',', ' ')
    salary_to = f"{int(float(salary_to)):,}".replace(',', ' ')
    salary_gross = "Без вычета налогов" if salary_gross == "True" else "С вычетом налогов"
    salary_currency = currency[salary_currency]
    return f"{salary_from} - {salary_to} ({salary_currency}) ({salary_gross})"

def formatter(vacancies):
    formatted_vacancies = []
    for vacancy in vacancies:
        result = {}
        result['Название'] = vacancy['name']
        result['Описание'] = vacancy['description'].rstrip()
        result['Навыки'] = ', '.join(vacancy['key_skills'].split('\n'))
        result['Опыт работы'] = work_experience[vacancy['experience_id']]
        result['Премиум-вакансия'] = "Да" if vacancy['premium'] == "True" else "Нет"
        result['Компания'] = vacancy['employer_name']
        result['Оклад'] = get_salary(vacancy['salary_from'],vacancy['salary_to'],
            vacancy['salary_gross'],vacancy['salary_currency'])
        result['Название региона'] = vacancy['area_name']
        result['Дата публикации вакансии'] = vacancy['published_at']

        formatted_vacancies.append(result)
    return formatted_vacancies

def create_table(vacancies):
    if not len(vacancies):
        return "Нет данных"

    table = PrettyTable()
    table.field_names = ["№"] + [title for title in vacancies[0].keys()]
    table.max_width = 20
    table.align = "l"
    fill_table(table, vacancies)
    return table

def fill_table(table, vacancies):
    for i in range(len(vacancies)):
        row = [info if len(info) <= 100 else info[:100] + "..." for info in vacancies[i].values()]
        number = i + 1
        row.insert(0, number)
        table.add_row(row, divider=True)

def main():
    file_name = input()
    vacancies = сsv_reader(file_name)
    formatted_vacancies = formatter(vacancies)
    table = create_table(formatted_vacancies)
    print(table)

if __name__ == "__main__":
    main()