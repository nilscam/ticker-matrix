import src.data.crypto as stock
import src.data.crypto as crypto
from ticker.src.display import TickerDisplay


# async def run_epoch():
#     while True:
#         runner.run_epoch()
#         await asyncio.sleep(1 / 2)  # 60 fps


# loop = asyncio.get_event_loop()
# loop.create_task(self.refresh_data())


class Ticker:
    def __init__(self) -> None:
        self.is_running = False
        self.stock_data = stock.get_stock_data()
        self.crypto_data = crypto.get_crypto_data()
        self.displayer = TickerDisplay()

    def set_running(self, is_running: bool) -> None:
        self.is_running = is_running

    def run_epoch(self):
        if self.is_running:
            self.displayer.run_epoch()

    def refresh_data(self):
        self.stock_data = stock.get_stock_data()
        self.crypto_data = crypto.get_crypto_data()