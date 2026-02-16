from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/vacancies/{vacancy_id}")
def read_data(vacancy_id):
    conn = sqlite3.connect('vacancies.db')
    query = f"SELECT id, name, salary, area_name, published_at FROM vacancies WHERE id = {vacancy_id}"
    cursor = conn.execute(query)
    name = cursor[1]
    salary = cursor[2]
    area_name = cursor[3]
    published_at = cursor[4]
    conn.close()
    return {'id': vacancy_id, 'name': name, 'salary': salary, 'area_name': area_name, 'published_at': published_at}


@app.post("/vacancies")
def write_data(vac):
    conn = sqlite3.connect('vacancies.db')
    query = f"""
        INSERT INTO vacancies
        (name, salary, area_name, published_at)
        VALUES ({vac['name']},{vac['salary']},{vac['area_name']}, '2023-07-23T21:31:51')
        """
    cursor = conn.execute(query)
    conn.close()
    return {"message": "vacancy posted successfully"}


@app.delete("/vacancies/{vacancy_id}")
def delete_data(vacancy_id):
    conn = sqlite3.connect('vacancies.db')
    query = f"DELETE FROM vacancies WHERE id = {vacancy_id}"
    cursor = conn.execute(query)
    conn.close()
    if cursor.rowcount > 0:
        return {"message": "vacancy deleted successfully"}
    return {"error": "vacancy not found"}
