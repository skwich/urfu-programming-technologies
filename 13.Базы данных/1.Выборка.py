import sqlite3

database = input()
table = input()

conn = sqlite3.connect(f"./{database}")

query = f"SELECT id, name FROM {table} WHERE gender LIKE 'male%' AND height > 1.8 ORDER BY name ASC"
cursor = conn.execute(query)

for row in cursor:
    id = row[0]
    name = row[1]
    print(f"{id} {name}")
