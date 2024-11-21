import pandas as pd
import openpyxl as op


def get_vacancies(filename):
    return pd.read_csv(
        "vacancies.csv", names=["name", "s_from", "s_to", "s_cur", "city", "data"]
    )


def create_statistics_of_years(wb, vacs):
    


def create_statistics_of_city(wb, vacs):
    pass


def create_report():
    csv = "vacancies.csv"
    vacs = get_vacancies(csv)
    wb = op.Workbook()
    create_statistics_of_years(wb, vacs)
    create_statistics_of_city(wb, vacs)
    wb.save("student_works/report.xlsx")


create_report()
