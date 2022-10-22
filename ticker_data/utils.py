##
# utils.py
##

# Format data
def format_data(data):
    formatted_data = {
        "value": data.get("close"),
        "evolution": (data.get("open") - data.get("close")) / data.get("open")
    }

    return formatted_data
