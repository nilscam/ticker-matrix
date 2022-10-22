##
# data_manager/api.py
##

# Imports
import requests
import datetime
from config import API_ENDPOINT, API_KEY, API_STOCK_URL, API_CRYPTO_URL
from config import CURRENCY

# Call API
def call_api(url):
    full_url = API_ENDPOINT + url + "?apiKey=" + API_KEY
    headers = {
        "Content-Type": "application/json",
        "X-Polygon-Key": API_KEY
    }
    response = requests.get(full_url, headers=headers)
    data = response.json()
    return (data)

# Call Stock API
def call_stock_api(stock):
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    url = API_STOCK_URL.format(stocksTicker=stock, date=yesterday)
    data = call_api(url)
    return data

# Call Crypto API
def call_crypto_api(crypto):
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    url = API_CRYPTO_URL.format(cryptoTicker=crypto, to=CURRENCY, date=yesterday)
    data = call_api(url)
    return data
