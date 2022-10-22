##
# main.py
##

# Imports
import display
import data_manager.main as data_manager
import format_market_data from utils

# Main
def main():
    data = data_manager.get_data()
    message_to_display = format_market_data(data)
    display.run_text(message_to_display)


# Launcher
if __name__ == "__main__":
    main()
