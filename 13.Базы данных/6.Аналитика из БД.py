import pandas as pd
import sqlite3


database_name = input()
table_name = input()
vac_name = input()

conn = sqlite3.connect(database_name)

df_years_salary = pd.read_sql(f"""
        SELECT strftime('%Y', published_at) as 'Год', ROUND(AVG(salary), 2) as 'Средняя з/п'
        FROM {table_name}
        GROUP BY Год
    """, conn)


df_years_count = pd.read_sql(f"""
        SELECT strftime('%Y', published_at) as 'Год', COUNT(name) as 'Количество вакансий'
        FROM {table_name}
        WHERE salary IS NOT NULL
        GROUP BY Год 
    """, conn)


df_years_salary_vac = pd.read_sql(f"""
        SELECT strftime('%Y', published_at) as 'Год', ROUND(AVG(salary), 2) as 'Средняя з/п - {vac_name}'
        FROM {table_name}
        WHERE name LIKE '{vac_name}%'
        GROUP BY Год
    """, conn)


df_years_count_vac = pd.read_sql(f"""
        SELECT strftime('%Y', published_at) as 'Год', COUNT(name) as 'Количество вакансий - {vac_name}'
        FROM {table_name}
        WHERE name LIKE '{vac_name}%' AND salary IS NOT NULL
        GROUP BY Год
    """, conn)


df_area_salary = pd.read_sql(f"""
        SELECT area_name as 'Город', ROUND(AVG(salary), 2) as 'Уровень зарплат по городам'
        FROM {table_name}
        GROUP BY Город
        HAVING FLOOR(COUNT(*) / (SELECT COUNT(*) * 0.008 FROM {table_name})) >= 1
        ORDER BY AVG(salary) DESC, Город DESC
        LIMIT 10
    """, conn)


df_area_count = pd.read_sql(f"""
        SELECT area_name as 'Город', (COUNT(*) * 1.0 / (SELECT COUNT(*) FROM {table_name})) as 'Доля вакансий'
        FROM {table_name}
        GROUP BY Город
        HAVING FLOOR(COUNT(*) / (SELECT COUNT(*) * 0.008 FROM {table_name})) >= 1
        ORDER BY COUNT(*) / (SELECT COUNT(*) * 0.008 FROM {table_name}) DESC
        LIMIT 10
    """, conn)
