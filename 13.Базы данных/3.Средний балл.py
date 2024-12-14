import sqlite3

database = input()
table = input()
mark_table = input()

conn = sqlite3.connect(database)

query = f"""
    SELECT {table}.name, ROUND(AVG({mark_table}.mark), 0) AS average
    FROM {table}
    JOIN {mark_table} ON {table}.id = {mark_table}.id
    GROUP BY {table}.id
    ORDER BY {table}.id
"""

result = conn.execute(query).fetchall()

for row in result:
    print(f"{row[0]} {row[1]}")
