##
# data_manager/config.py
##

# Imports
import os
from dotenv import load_dotenv

load_dotenv()

# API VARIABLES
API_ENDPOINT = "https://api.polygon.io"
API_KEY = os.getenv('API_KEY')

API_STOCK_URL = "/v1/open-close/{stocksTicker}/{date}"
API_CRYPTO_URL = "/v1/open-close/crypto/{cryptoTicker}/{to}/{date}"

# STOCK VARIABLES
APPLE = "AAPL"
GOOGLE = "GOOG"
NETFLIX = "NFLX"

# CRYPTO VARIABLES
BTC = "BTC"
ETH = "ETH"

# CURRENCY
CURRENCY = "USD"
