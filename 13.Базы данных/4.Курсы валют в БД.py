import pandas as pd
import sqlite3


database_name = input()
csv_file = input()
table_name = input()


df = pd.read_csv(csv_file, encoding="utf-8-sig")
conn = sqlite3.connect(database_name)
df.to_sql(table_name, conn, index=False)
conn.close()
