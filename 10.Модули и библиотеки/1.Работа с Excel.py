import pandas as pd
import openpyxl as op


def get_vacancies(filename: str):
    return pd.read_csv("vacancies.csv", names=["name", "s_from", "s_to", "s_cur", "city", "date"])


def create_statistics_of_years(wb: op.Workbook, vacs: pd.DataFrame):
    wb.create_sheet("Статистика по годам", 0)
    sheet = wb[wb.sheetnames[0]]

    vacs["year"] = vacs["date"].apply(lambda x: x[:4])
    vacs["s_avg"] = vacs[["s_from", "s_to"]].mean(1)
    df = vacs.groupby("year", as_index=False).agg({"s_avg": "mean", "name": "count"})
    df["s_avg"] = df["s_avg"].round().astype(int)

    data = ["Год", "Средняя зарплата", "Количество вакансий"] + df.values.tolist()
    for i, row in enumerate(data, 1):
        year, salary, count = row
        sheet[f"A{i}"] = year
        sheet[f"B{i}"] = salary
        sheet[f"C{i}"] = count


def create_statistics_of_city(wb: op.Workbook, vacs: pd.DataFrame):
    wb.create_sheet("Статистика по городам")


def create_report():
    csv = "vacancies.csv"
    vacs = get_vacancies(csv)
    wb = op.Workbook()
    create_statistics_of_years(wb, vacs)
    create_statistics_of_city(wb, vacs)
    wb.save("student_works/report.xlsx")


create_report()
