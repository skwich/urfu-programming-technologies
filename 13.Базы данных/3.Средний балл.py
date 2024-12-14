import sqlite3

database = input()
table = input()
mark_table = input()

conn = sqlite3.connect(database)

query = f"""
    SELECT {table}.*, 
    FROM {table}
    INNER JOIN {mark_table} ON {table}.id = {mark_table}.id
"""
