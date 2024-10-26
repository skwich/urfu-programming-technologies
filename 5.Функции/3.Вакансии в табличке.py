from prettytable import PrettyTable
import csv

dictionary = {
    "name": "Название",
    "description": "Описание",
    "key_skills": "Навыки",
    "experience_id": "Опыт работы",
    "premium": "Премиум-вакансия",
    "employer_name": "Компания",
    "salary": "Оклад",
    "area_name": "Название региона",
    "published_at": "Дата публикации вакансии"
}

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
    titles = []
    vacancies = []
    with open(file_name, encoding='utf_8_sig') as csv_file:
        reader = csv.reader(csv_file)
        titles = next(reader)
        for row in reader:
            vacancies += [row]
    return (vacancies, titles)

def formatter(vacancies, titles):
    formatted_vacancies = []
    for vacancy in vacancies:
        result = {}
        salary_from = 0
        salary_to = 0
        salary_gross = ""
        salary_currency = ""
        for (key, value) in zip(titles, vacancy):
            value = value.rstrip()

            match key:
                case 'key_skills':
                    result[dictionary[key]] = ', '.join(value.split('\n'))
                case 'experience_id':
                    result[dictionary[key]] = work_experience[value]
                case 'premium':
                    result[dictionary[key]] = "Да" if value == "True" else "Нет"
                case 'salary_from':
                    salary_from = f"{int(float(value)):,}".replace(',', ' ')
                case 'salary_to':
                    salary_to = f"{int(float(value)):,}".replace(',', ' ')
                case 'salary_gross':
                    salary_gross = "Без вычета налогов" if value == "True" else "С вычетом налогов"
                case 'salary_currency':
                    salary_currency = currency[value]
                case _:
                    result[dictionary[key]] = value

        result["Оклад"] = f"{salary_from} - {salary_to} ({salary_currency}) ({salary_gross})"
        result["Название региона"] = result.pop("Название региона")
        result["Дата публикации вакансии"] = result.pop("Дата публикации вакансии")

        formatted_vacancies.append(result)

    return formatted_vacancies

def create_table(vacancies: list):
    table = PrettyTable()
    table.field_names = ["№"] + [title for title in dictionary.values()]
    table.max_width = 20
    table.align = "l"

    if len(vacancies):
        fill_table(table, vacancies)
    else:
        table = "Нет данных"

    return table

def fill_table(table, vacancies):
    for i in range(len(vacancies)):
        row = [info if len(info) <= 100 else info[:100] + "..." for info in vacancies[i].values()]
        number = i + 1
        row.insert(0, number)
        table.add_row(row, divider=True)

def main():
    file_name = input()
    vacancies, titles = сsv_reader(file_name)
    formatted_vacancies = formatter(vacancies, titles)
    table = create_table(formatted_vacancies)
    print(table)

if __name__ == "__main__":
    main()