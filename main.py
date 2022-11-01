import sys

# Append path for every feature
sys.path.append("./ticker")
sys.path.append("./message_printer")


import asyncio
from enum import Enum
from pydantic import BaseModel

from fastapi import FastAPI
from ticker.feature import Ticker
from message_printer.feature import MessagePrinter

app = FastAPI()


class MatrixModes(str, Enum):
    TICKER = "ticker"
    MESSAGE_PRINTER = "message_printer"


class MatrixRunner:
    def __init__(self) -> None:
        self.mode = MatrixModes.TICKER
        self.is_running = False
        self.ticker = Ticker()
        self.message_printer = MessagePrinter("No text defined")

    def set_running(self, is_running: bool) -> None:
        self.is_running = is_running

    def run_epoch(self):
        if self.is_running:
            if self.mode == MatrixModes.TICKER:
                self.ticker.run_epoch()
            elif self.mode == MatrixModes.MESSAGE_PRINTER:
                self.message_printer.run_epoch()

    def set_message_printer_mode(self, message):
        self.mode = MatrixModes.MESSAGE_PRINTER
        self.message_printer.set_message(message)

    def set_ticker_mode(self):
        self.mode = MatrixModes.TICKER


runner = MatrixRunner()


async def run_epoch():
    while True:
        runner.run_epoch()
        await asyncio.sleep(1 / 20)  # 60 fps


loop = asyncio.get_event_loop()
loop.create_task(run_epoch())


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/run")
def run():
    runner.set_running(True)
    return {"running": True}


@app.post("/stop")
def mode():
    runner.set_running(False)
    return {"running": False}


@app.put("/ticker")
def set_mode_ticker():
    runner.set_ticker_mode()
    return {"mode_set": "ticker"}


class MessagePrinterBody(BaseModel):
    message: str


@app.put("/message_printer")
def set_mode_message_printer(body: MessagePrinterBody):
    runner.set_message_printer_mode(body.message)
    return {"mode_set": "message_printer"}
