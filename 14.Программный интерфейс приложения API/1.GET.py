import requests
import asyncio
import json

area_name = input()
BASE_URL = "http://127.0.0.1:8000"
vac_id = 1

async def main():
    while True:
        res = await requests.get(f'{BASE_URL}/{vac_id}')
        if "error" in res.text:
            break
        result = json.loads(res.text)
        if area_name == str(result.get('area_name')):
            print(result)
        vac_id += 1

main()