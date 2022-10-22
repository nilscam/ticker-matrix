##
# data_manager/main.py
##

# Imports
import data_manager.stock as stock
import data_manager.crypto as crypto

# Get Data
def get_data():
    stock_data = stock.get_stock_data()
    crypto_data = crypto.get_crypto_data()

    return {
        "stock": stock_data,
        "crypto": crypto_data
    }
