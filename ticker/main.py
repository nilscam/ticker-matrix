##
# main.py
##

# Imports
# import src.display as display
from src.utils import format_market_data_to_display

import src.data.stock as stock
import src.data.crypto as crypto

# Main
def main():
    stock_data = stock.get_stock_data()
    crypto_data = crypto.get_crypto_data()

    print(stock_data)
    print(crypto_data)

    message_to_display = format_market_data_to_display(
        stock_data
    ) + format_market_data_to_display(crypto_data)
    print(message_to_display)
    # display.run_text(message_to_display)


# Launcher
if __name__ == "__main__":
    main()
