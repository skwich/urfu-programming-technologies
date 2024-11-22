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

    data = [["Год", "Средняя зарплата", "Количество вакансий"]] + df.values.tolist()
    for i, row in enumerate(data, 1):
        year, salary, count = row
        sheet[f"A{i}"] = year
        sheet[f"B{i}"] = salary
        sheet[f"C{i}"] = count


def create_statistics_of_city(wb: op.Workbook, vacs: pd.DataFrame):
    wb.create_sheet("Статистика по городам", index=1)
    sheet = wb[wb.sheetnames[1]]
    
    vacs["s_avg"] = vacs[["s_from", "s_to"]].mean(1)
    
    vacs["s_avg"] = vacs[["s_from", "s_to"]].mean(1)
    stat = (vacs
            .groupby('city', as_index=False)[['city','name', 's_avg']]
            .agg({'city':'first', 'name':'count', 's_avg':'mean'})
            .sort_values('name', ascending=False)
    )
    stat['s_avg'] = stat['s_avg'].round().astype(int)
    stat["name"] = (stat["name"] / len(vacs) * 100).round(2)
    
    salaries = (stat[stat['name'] >= 1].sort_values('s_avg', ascending=False))[['city','s_avg']].values[:10].tolist()
    for i, row in enumerate([["Город", "Уровень зарплат"]] + salaries, 1):
        city, salary = row
        sheet[f"A{i}"] = city
        sheet[f"B{i}"] = salary
    
    shares = (stat[stat["name"] >= 1].sort_values("name", ascending=False))[["city", "name"]].values[:10].tolist()
    for i, row in enumerate([["Город", "Доля вакансий, %"]] + shares, 1):
        city, share = row
        sheet[f"D{i}"] = city
        sheet[f"E{i}"] = share


def create_report():
    csv = "vacancies.csv"
    vacs = get_vacancies(csv)
    wb = op.Workbook()
    create_statistics_of_years(wb, vacs)
    create_statistics_of_city(wb, vacs)
    wb.save("student_works/report.xlsx")
    wb.close()


create_report()
