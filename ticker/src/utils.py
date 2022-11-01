##
# utils.py
##
from config import CRYPTO_LIST, STOCK_LIST
from config import ARROW_UP, ARROW_DOWN

market_list = {"stock": STOCK_LIST, "crypto": CRYPTO_LIST}

def format_market_data_to_display(data):
    formatted_url = ""
    for stock in data:
        formatted_url += f"{stock['asset']} : ${stock['value']} ({ARROW_UP if stock['return'] > 0 else ARROW_DOWN} {stock['return']} %) "
    return formatted_url


def format_data_from_api(asset: str, data: dict):
    print(data)
    formatted_data = {
        "asset": asset,
        "value": data.get("close"),
        "return": round(
            ((data.get("close") - data.get("open")) / data.get("open")) * 100, 2
        ),
    }

    return formatted_data
