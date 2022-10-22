##
# main.py
##

# Imports
import display
import data_manager.main as data_manager

# Main
def main():
    data = data_manager.get_data()
    display.message(data)

# Launcher
if __name__ == '__main__':
    main()
