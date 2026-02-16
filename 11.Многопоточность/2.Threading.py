from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup


def get_currencies(url, id, currencies):
    response = requests.get(url)
    if response.status_code == 200:
        secret_code()
        soup = BeautifulSoup(response.text, "html.parser")
        currency = str(soup.find_all("valute")[id])
        if currency not in currencies:
            currencies.append(currency)


if __name__ == "__main__":
    currencies = []
    id = int(input())

    for url in urls:
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.submit(get_currencies, url, id, currencies)

    currencies_string = "".join(currencies)
    print(currencies_string)
