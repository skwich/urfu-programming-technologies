import csv
from datetime import datetime


currency_to_rub = {
    "Манаты": 35.68,
    "Белорусские рубли": 23.91,
    "Евро": 59.90,
    "Грузинский лари": 21.74,
    "Киргизский сом": 0.76,
    "Тенге": 0.13,
    "Рубли": 1,
    "Гривны": 1.64,
    "Доллары": 60.66,
    "Узбекский сум": 0.0055,
}


class Vacancy:
    def __init__(self, vacancy):
        self.name           = vacancy['name']
        self.salary         = Salary(vacancy['salary_from'],vacancy['salary_to'],
                                     vacancy['salary_gross'],vacancy['salary_currency'])
        self.area_name      = vacancy['area_name']
        self.published_at   = vacancy['published_at']


class Salary:
    def __init__(self, salary_from, salary_to, salary_gross, salary_currency):
        self.salary_from     = salary_from
        self.salary_to       = salary_to
        self.salary_gross    = salary_gross
        self.salary_currency = salary_currency
        self.average = (float(self.salary_from) + float(self.salary_to)) / 2
        self.average *= currency_to_rub[self.salary_currency]


class DataSet:
    def __init__(self, filename) -> list:
        with open(filename, encoding="utf-8-sig") as csv_file:
            self.reader = csv.reader(csv_file)
            self.titles = next(self.reader)
            vacancies = []
            for row in self.reader:
                gen = {key:value for (key,value) in zip(self.titles, row)}
                vacancies.append(gen)
            self.vacancies  = [Vacancy(vacancy) for vacancy in vacancies]


class Statistics:
    def __init__(self, dataset):
        self.dataset = dataset
        self.salary_dynamics = SalaryDynamics(dataset.vacancies)

    def get_salary_stat(self, profession_name):
        print(f"Средняя зарплата по годам: {self.salary_dynamics.GetAvgSalaryOfYears()}")
        print(f"Количество вакансий по годам: {self.salary_dynamics.count_of_vacancies}")
        print(f"Средняя зарплата по годам для профессии '{profession_name}': {self.salary_dynamics.GetAvgProfSalaryOfYears(profession_name)}")
        print(f"Количество вакансий по годам для профессии '{profession_name}': {self.salary_dynamics.count_of_prof}")
        print(f"Средняя зарплата по городам: {self.salary_dynamics.GetAvgOfCity()}")
        print(f"Доля вакансий по городам: {self.salary_dynamics.GetRateByCity()}")


class SalaryDynamics:
    def __init__(self, vacancies):
        self.dynamics = self.__GetDynamics(vacancies)
        self.vacancies = vacancies
        self.avg_salary = {}
        self.count_of_vacancies = {}
        self.avg_prof_salary = {}
        self.count_of_prof = {}
        self.avg_of_city = {}
        self.count_of_cities = {}
        self.rate_by_city = {}

    def __GetDynamics(self, vacancies):
        dynamics = self.__GetYears(vacancies)
        for vacancy in vacancies:
            data = {}
            data['name'] = vacancy.name
            data['salary'] = vacancy.salary.average
            data['area_name'] = vacancy.area_name
            dynamics[Utils.GetYear(vacancy.published_at)] += [data]
        return dynamics

    def __GetYears(self, vacancies):
        years = {}
        for vacancy in vacancies:
            year = Utils.GetYear(vacancy.published_at)
            years[year] = []
        return dict(sorted(years.items()))

    def GetAvgSalaryOfYears(self):
        for (year, vacancies) in self.dynamics.items():
            self.count_of_vacancies[year] = len(vacancies)
            self.avg_salary[year] = round(sum([vacancy['salary'] for vacancy in vacancies]) / self.count_of_vacancies[year])
        return self.avg_salary
    
    def GetAvgProfSalaryOfYears(self, prof_name):
        for (year, vacancies) in self.dynamics.items():
            count = sum(1 for vacancy in vacancies if prof_name.lower() in vacancy['name'].lower())
            if count != 0:
                self.count_of_prof[year] = count
                self.avg_prof_salary[year] = round(sum([vacancy['salary'] for vacancy in vacancies if prof_name.lower() in vacancy['name'].lower()]) / count)
        return self.avg_prof_salary
    
    def GetAvgOfCity(self):
        for vacancies in self.dynamics.values():
            for vacancy in vacancies:
                if self.avg_of_city.__contains__(vacancy['area_name']):
                    self.avg_of_city[vacancy['area_name']] += vacancy['salary']
                    self.count_of_cities[vacancy['area_name']] += 1
                else:
                    self.avg_of_city[vacancy['area_name']] = vacancy['salary']
                    self.count_of_cities[vacancy['area_name']] = 1
        self.avg_of_city = {key:round(salary/count) for (count, (key,salary)) in zip(self.count_of_cities.values(), self.avg_of_city.items())}
        self.avg_of_city = dict(sorted(self.avg_of_city.items(), key=lambda x: x[1], reverse=True))
        return dict(list(self.avg_of_city.items())[:10])

    def GetRateByCity(self):
        for vacancy in self.vacancies:
            city = vacancy.area_name
            self.rate_by_city[city] = round(self.count_of_cities[city]/sum(self.count_of_vacancies.values()), 4)
        self.rate_by_city = dict(sorted(self.rate_by_city.items(), key=lambda x: x[1], reverse=True)).items()
        return dict(list(self.rate_by_city)[:10])


class Utils:
    @staticmethod
    def GetYear(date):
        return datetime.strptime(date, "%H:%M:%S %d/%m/%Y").year


def main():
    filename = input()
    profession_name = input()
    dataset = DataSet(filename)
    statistics = Statistics(dataset)
    statistics.get_salary_stat(profession_name)


if __name__ == '__main__':
    main()