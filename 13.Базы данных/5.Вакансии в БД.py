import math
import pandas as pd
import sqlite3


def preproccessing(x):
    salary, currency, date = x["salary"], x["salary_currency"], x["published_at"][:7]
    if salary > 0 and currency is not None:
        query = f"SELECT {currency} FROM {currency_table} WHERE date LIKE '{date}%'"
        result = conn.execute(query).fetchone()[0]
        if result is None:
            return None
        return math.floor(salary * result)
    return None


database_name = input()
csv_file = input()
table_name = input()
currency_table = input()


conn = sqlite3.connect(database_name)

df = pd.read_csv(csv_file, encoding="utf-8-sig")
df["salary"] = df[["salary_from", "salary_to"]].mean(axis=1)
df["salary"] = df.apply(preproccessing, axis=1)
df["published_at"] = pd.to_datetime(df["published_at"]).apply(lambda x: pd.to_datetime(x).isoformat())
df = df[["name", "salary", "area_name", "published_at"]]

df.to_sql(table_name, conn, index=False)
conn.close()
