import requests

area_name = input()
BASE_URL = "http://127.0.0.1:8000/vacancies"
vac_id = 1

while True:
    response = requests.get(f'{BASE_URL}/{vac_id}')
    if "error" in response.text:
        break
    result = response.json()
    if result['area_name'] == area_name:
        print(result)
    vac_id += 1