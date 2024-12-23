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

def print_vacancies(vacancies, titles):
    for vacancy in vacancies:
        row = {}
        for (title, info) in zip(titles, vacancy):
            row[title] = info

        for key, value in formatter(row).items():
            print(f"{dictionary[key]}: {value}")

        if vacancy != vacancies[-1]:
            print()

def formatter(row):
    result = {}

    for key, value in row.items():
        value = value.rstrip()

        match key:
            case 'key_skills':
                result[key] = ', '.join(value.split('\n'))
            case 'experience_id':
                result[key] = work_experience[value]
            case 'premium':
                result[key] = "Да" if value == "True" else "Нет"
            case 'salary_from' | 'salary_to':
                result[key] = '{0:,}'.format(int(float(value))).replace(',', ' ')
            case 'salary_gross':
                result[key] = "Без вычета налогов" if value == "True" else "С вычетом налогов"
            case 'salary_currency':
                result[key] = currency[value]
            case _:
                result[key] = value
    
    result['salary'] = f"{result.pop('salary_from')} - {result.pop('salary_to')} ({result.pop('salary_currency')}) ({result.pop('salary_gross')})"
    result['area_name'] = result.pop('area_name')
    result['published_at'] = result.pop('published_at')
    
    return result

vacancies, titles = сsv_reader(input())
print_vacancies(vacancies, titles)