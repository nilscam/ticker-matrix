import sys

# Append path for every feature
sys.path.append("./ticker")


import asyncio
from enum import Enum

from fastapi import FastAPI
from ticker.ticker import Ticker

app = FastAPI()


class MatrixModes(str, Enum):
    TICKER = "ticker"
    CLOCK = "clock"


class MatrixRunner:
    def __init__(self) -> None:
        self.mode = MatrixModes.TICKER
        self.is_running = False
        self.ticker = Ticker()

    def set_mode(self, mode: str) -> None:
        self.mode = mode

    def run_epoch(self):
        if self.is_running:
            if self.mode == MatrixModes.TICKER:
                self.ticker.run_epoch()
            elif self.mode == MatrixModes.CLOCK:
                print("clock", flush=True)

    def set_running(self, is_running: bool) -> None:
        self.is_running = is_running


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


@app.put("/{mode}")
def set_mode(mode: MatrixModes):
    runner.set_mode(mode)
    return {"mode_set": mode}
