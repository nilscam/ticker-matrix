#!/usr/bin/env python
# Display a runtext with double-buffering.
import sys
from lib.matrix_connector import MatrixConnector
from rgbmatrix import graphics
import time


# class RunText(MatrixConnector):
#     def __init__(self, *args, **kwargs):
#         super(RunText, self).__init__(*args, **kwargs)
#         self.parser.add_argument(
#             "-t",
#             "--text",
#             help="The text to scroll on the RGB LED panel",
#             default="Hello world!",
#         )

#     def run(self, message):
#         offscreen_canvas = self.matrix.CreateFrameCanvas()
#         font = graphics.Font()
#         font.LoadFont("lib/fonts/7x13.bdf")
#         textColor = graphics.Color(255, 255, 0)
#         pos = offscreen_canvas.width
#         # my_text = self.args.text
#         my_text = message

#         while True:
#             offscreen_canvas.Clear()
#             len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)
#             pos -= 1
#             if pos + len < 0:
#                 pos = offscreen_canvas.width

#             time.sleep(0.05)
#             offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# # Main function
# def run_text(message):
#     print("message displaying on matrix : ", message)
#     run_text = RunText()
#     if not run_text.connect():
#         run_text.print_help()
#     try:
#         # Start loop
#         print("Press CTRL-C to stop sample")
#         run_text.run(message)
#     except KeyboardInterrupt:
#         print("Exiting\n")
#         sys.exit(0)


#!/usr/bin/env python
# Display a runtext with double-buffering.
import sys
from lib.matrix_connector import MatrixConnector
from rgbmatrix import graphics
import time


class TickerDisplay(MatrixConnector):
    def __init__(self, text):
        self.connect()  # connect to matrix api, extend of MatrixConnector
        self.offscreen_canvas = self.matrix.CreateFrameCanvas()
        self.pos = self.offscreen_canvas.width

        self.font = graphics.Font()
        try:
            self.font.LoadFont("lib/fonts/7x13.bdf")
        except:
            self.font.LoadFont("ticker/lib/fonts/7x13.bdf")
        self.textColor = graphics.Color(255, 255, 0)

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


# Demo function
def demo_ticker_display(message):
    print("message displaying on matrix : ", message)
    ticker_display = TickerDisplay(message)
    # if not ticker_display.connect():
    #     ticker_display.print_help()
    try:
        # Start loop
        print("Press CTRL-C to stop sample")
        while True:
            ticker_display.run_epoch()
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("Exiting\n")
        sys.exit(0)
