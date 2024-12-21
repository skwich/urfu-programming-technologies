import requests

BASE_URL = 'http://127.0.0.1:8000/vacancies'
name = input()
salary = input()
area_name = input()
post_query = {
    "name": name,
    "salary": salary,
    "area_name": area_name
}

response = requests.post(BASE_URL, json=post_query)