import sqlite3

database = input()
table = input()

conn = sqlite3.connect(f"./{database}")

query = f"""
    SELECT gender, ROUND(AVG(height), 2), SUM(weight)
    FROM {table}
    GROUP BY gender
"""
result = conn.execute(query).fetchall()

for row in result:
    gender = row[0]
    avg_height = row[1]
    total_weight = row[2]
    print(f"{gender} {avg_height} {total_weight}")
