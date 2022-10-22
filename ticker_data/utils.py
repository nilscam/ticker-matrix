##
# utils.py
##

# Imports
from config import APPLE, GOOGLE, NETFLIX, BTC, ETH

market_list = {
    "stock": [
        APPLE,
        GOOGLE,
        NETFLIX
    ],
    "crypto": [
        BTC,
        ETH
    ]
}

# Format Market Data


def format_market_data(data):
    formatted_url = ""

    for stock in market_list.get("stock"):
        formatted_url += stock + " : $" + str(data.get("stock").get(stock).get("value")) + " (" + str(
            round(data.get("stock").get(stock).get("evolution") * 100, 2)) + "%) "
    for crypto in market_list.get("crypto"):
        formatted_url += crypto + " : $" + str(data.get("crypto").get(crypto).get(
            "value")) + " (" + str(round(data.get("crypto").get(crypto).get("evolution") * 100, 2)) + "%) "
    return formatted_url

# Format data


def format_data(data):
    formatted_data = {
        "value": data.get("close"),
        "evolution": (data.get("close") - data.get("open")) / data.get("open")
    }

    return formatted_data
