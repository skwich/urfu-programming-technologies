import csv
from prettytable import PrettyTable, ALL


class Vacancy:
    def __init__(self, vacancy):
        self.name           = vacancy[0]
        self.description    = vacancy[1]
        self.key_skills     = vacancy[2]
        self.experience_id  = vacancy[3]
        self.premium        = vacancy[4]
        self.employer_name  = vacancy[5]
        self.salary         = Salary(vacancy[6],vacancy[7],vacancy[8],vacancy[9])
        self.area_name      = vacancy[10]
        self.published_at   = vacancy[11]

    def GetVacancyFields(self):
        return [
            self.name,
            Utils.format_data(self.description),
            Utils.format_data(self.key_skills),
            self.experience_id,
            self.premium,
            self.employer_name,
            self.salary.salary_from,
            self.salary.salary_to,
            self.salary.salary_gross,
            self.salary.salary_currency,
            self.area_name,
            self.published_at
        ]


class Salary:
    def __init__(self, salary_from, salary_to, salary_gross, salary_currency):
        self.salary_from     = salary_from
        self.salary_to       = salary_to
        self.salary_gross    = salary_gross
        self.salary_currency = salary_currency


class DataSet:
    def __init__(self, filename):
        with open(filename, encoding="utf-8-sig") as csv_file:
            self.reader = csv.reader(csv_file)
            self.titles = next(self.reader)
            gen = [row for row in self.reader]
            self.vacancies  = [Vacancy(vacancy) for vacancy in gen]


class Utils:
    @staticmethod
    def create_table(dataset):
        table = PrettyTable()
        table.field_names = ['№'] + list(dataset.titles)
        table.max_width = 20
        table.hrules = ALL
        table.align = 'l'
        for i, vacancy in enumerate(dataset.vacancies, 1):
            table.add_row([i] + vacancy.GetVacancyFields())
        return table
    
    @staticmethod
    def format_data(data):
        return data if len(data) <= 100 else data[:100] + "..."


def main():
    filename = input()
    dataset = DataSet(filename)
    table = Utils.create_table(dataset)
    print(table)


if __name__ == '__main__':
    main()