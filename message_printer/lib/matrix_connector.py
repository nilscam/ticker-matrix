from rgbmatrix import RGBMatrix, RGBMatrixOptions


class MatrixConnector(object):
    def __init__(self):
        print("MatrixConnector message printer init")
        options = RGBMatrixOptions()

        options.rows = 64
        options.cols = 64
        options.chain_length = 2
        options.parallel = 1
        options.gpio_slowdown = 3
        options.hardware_mapping = "adafruit-hat"

        options.row_address_type = 0
        options.multiplexing = 0
        options.pwm_bits = 11
        options.brightness = 100
        options.pwm_lsb_nanoseconds = 130
        options.led_rgb_sequence = "RGB"
        options.pixel_mapper_config = ""
        options.panel_type = ""

        self.matrix = RGBMatrix(options=options)
