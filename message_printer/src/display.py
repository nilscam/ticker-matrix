#!/usr/bin/env python
# Display a runtext with double-buffering.
import sys

sys.path.append("../..")  # to import lib

from lib.matrix_connector import matrix
from rgbmatrix import graphics


class MessagePrinterDisplay:
    def __init__(self, text):
        self.matrix = matrix
        self.offscreen_canvas = self.matrix.CreateFrameCanvas()
        self.pos = self.offscreen_canvas.width

        self.font = graphics.Font()
        # try:
        self.font.LoadFont("lib/fonts/7x13.bdf")
        # except:
        #     self.font.LoadFont("ticker/lib/fonts/7x13.bdf")
        self.textColor = graphics.Color(255, 0, 255)

        self.text_to_display = text

    def set_text_to_display(self, text):
        self.text_to_display = text

    def run_epoch(self):
        self.offscreen_canvas = self.matrix.SwapOnVSync(self.offscreen_canvas)
        self.offscreen_canvas.Clear()

        #   draw
        len = graphics.DrawText(
            self.offscreen_canvas,
            self.font,
            self.pos,
            10,
            self.textColor,
            self.text_to_display,
        )

        self.pos -= 1
        if self.pos + len < 0:
            self.pos = self.offscreen_canvas.width
