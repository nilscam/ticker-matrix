##
# data_manager/stock.py
##

# Imports
from config import STOCK_LIST
import src.data.api as api
import src.utils as utils

# Get Stock Data
def get_stock_data():
    stock_data = []

    for stock in STOCK_LIST:
        data = api.call_stock_api(stock)
        stock_data.append(utils.format_data_from_api(stock, data))
    return stock_data
