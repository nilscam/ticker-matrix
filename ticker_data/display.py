#!/usr/bin/env python
# Display a runtext with double-buffering.
import sys
from lib.matrix_connector import MatrixConnector
from rgbmatrix import graphics
import time


class RunText(MatrixConnector):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument(
            "-t",
            "--text",
            help="The text to scroll on the RGB LED panel",
            default="Hello world!",
        )

    def run(self, message):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/7x13.bdf")
        textColor = graphics.Color(255, 255, 0)
        pos = offscreen_canvas.width
        # my_text = self.args.text
        my_text = message

        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)
            pos -= 1
            if pos + len < 0:
                pos = offscreen_canvas.width

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
def run_text(message):
    print("message displaying on matrix : ", message)
    run_text = RunText()
    if not run_text.connect():
        run_text.print_help()
    try:
        # Start loop
        print("Press CTRL-C to stop sample")
        run_text.run(message)
    except KeyboardInterrupt:
        print("Exiting\n")
        sys.exit(0)
