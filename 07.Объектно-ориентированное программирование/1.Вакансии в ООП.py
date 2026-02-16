import csv
from var_dump import var_dump


def csv_reader(filename):
    with open(filename, encoding="utf-8-sig") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        return [row for row in reader]


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


class Salary:
    def __init__(self, salary_from, salary_to, salary_gross, salary_currency):
        self.salary_from     = salary_from
        self.salary_to       = salary_to
        self.salary_gross    = salary_gross
        self.salary_currency = salary_currency


def main():
    filename = input()
    vacancies = [Vacancy(vacancy) for vacancy in csv_reader(filename)]
    var_dump(vacancies)


if __name__ == '__main__':
    main()