import csv

dictionary = {
    "name": "Название",
    "description": "Описание",
    "key_skills": "Навыки",
    "experience_id": "Опыт работы",
    "premium": "Премиум-вакансия",
    "employer_name": "Компания",
    "salary_from": "Нижняя граница вилки оклада",
    "salary_to": "Верхняя граница вилки оклада",
    "salary_gross": "Оклад указан до вычета налогов",
    "salary_currency": "Идентификатор валюты оклада",
    "area_name": "Название региона",
    "published_at": "Дата и время публикации вакансии"
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
        for (title, info) in zip(titles, vacancy):
            print(f"{dictionary[title]}: {format_info(info)}")

        if vacancy != vacancies[-1]:
            print()

def format_info(info):
    result = info.rstrip()

    if info.count('\n'):
        result = ', '.join(info.split('\n'))
    elif info in ("True", "False"):
        result = "Да" if info == "True" else "Нет"

    return result

vacancies, titles = сsv_reader(input())
print_vacancies(vacancies, titles)