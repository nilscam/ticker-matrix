##
# data_manager/crypto.py
##

# Imports
from config import CRYPTO_LIST
import src.data.api as api
import src.utils as utils

# Get Crypto Data
def get_crypto_data():
    crypto_data = []

    for crypto in CRYPTO_LIST:
        data = api.call_crypto_api(crypto)
        crypto_data.append(utils.format_data_from_api(crypto, data))
    return crypto_data
