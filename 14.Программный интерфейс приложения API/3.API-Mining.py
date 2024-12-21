import pandas as pd
import requests
from io import StringIO
from concurrent.futures import ThreadPoolExecutor

start_date = pd.to_datetime('2003-01-01')
end_date = pd.to_datetime('2024-11-01')
dates_range = pd.date_range(start_date, end_date, freq='MS').to_list()
BASE_URL = "https://www.cbr.ru/scripts/XML_daily.asp?date_req="
list_of_rows = []

with ThreadPoolExecutor(10) as executor:
    response = executor.map(requests.get, [f"{BASE_URL}{date.strftime('01/%m/%Y')}" for date in dates_range])
    for data in response:
        date = pd.to_datetime(data.url[data.url.find('=')+1:], dayfirst=True)
        df = pd.read_xml(StringIO(data.text))
        df = df[['CharCode', 'VunitRate']]
        df['VunitRate'] = df['VunitRate'].str.replace(',', '.').astype(float)
        df = df[df['CharCode'].isin(["BYR","USD","EUR","KZT","UAH","AZN","KGS","UZS","GEL"])].set_index('CharCode').T
        df.insert(0, 'date', date.strftime('%Y-%m'))
        list_of_rows.append(df.to_dict(orient='records')[0])

result = pd.DataFrame(list_of_rows)
result.to_csv("student_works/currency.csv", index=False)