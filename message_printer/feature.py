from message_printer.src.display import MessagePrinterDisplay


class MessagePrinter:
    def __init__(self, message) -> None:
        self.message = message
        self.displayer = MessagePrinterDisplay(message)

    def set_message(self, message):
        self.message = message
        self.displayer.set_text_to_display(message)

    def run_epoch(self):
        self.displayer.run_epoch()
