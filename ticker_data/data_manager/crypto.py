##
# data_manager/crypto.py
##

# Imports
from config import BTC, ETH
import data_manager.api as api
import utils

# Crypto
crypto_list = [
    BTC,
    ETH
]

# Get Crypto Data
def get_crypto_data():
    crypto_data = {}

    for crypto in crypto_list:
        data = api.call_crypto_api(crypto)
        crypto_data[crypto] = utils.format_data(data)
    return crypto_data
