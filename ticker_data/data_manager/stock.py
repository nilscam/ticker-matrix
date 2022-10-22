##
# data_manager/stock.py
##

# Imports
from config import APPLE, GOOGLE, NETFLIX
import data_manager.api as api
import utils

# Stocks
stock_list = [APPLE, GOOGLE, NETFLIX]

# Get Stock Data
def get_stock_data():
    stock_data = {}

    for stock in stock_list:
        data = api.call_stock_api(stock)
        stock_data[stock] = utils.format_data(data)
    return stock_data
