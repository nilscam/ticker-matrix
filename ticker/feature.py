import src.data.stock as stock
import src.data.crypto as crypto
from src.display import TickerDisplay
from src.utils import format_market_data_to_display


# async def run_epoch():
#     while True:
#         runner.run_epoch()
#         await asyncio.sleep(1 / 2)  # 60 fps


# loop = asyncio.get_event_loop()
# loop.create_task(self.refresh_data())


class Ticker:
    def __init__(self) -> None:
        self.stock_data = stock.get_stock_data()
        self.crypto_data = crypto.get_crypto_data()

        self.message_to_display = format_market_data_to_display(
            self.stock_data
        ) + format_market_data_to_display(self.crypto_data)

        self.displayer = TickerDisplay(self.message_to_display)

    def run_epoch(self):
        self.displayer.run_epoch()

    def refresh_data(self):
        self.stock_data = stock.get_stock_data()
        self.crypto_data = crypto.get_crypto_data()
