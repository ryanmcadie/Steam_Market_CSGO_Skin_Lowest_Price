import requests
from requests.utils import quote

def get_item_price(item):
    # Define the URL for the Steam Marketplace API
    url = f"https://steamcommunity.com/market/priceoverview/?currency=20&appid=730&market_hash_name={quote(item)}"

    # Make a GET request to the API
    response = requests.get(url)

    # Check if the response was successful
    if response.status_code != 200:
        print(f"Error: The API returned a status code of {response.status_code}")
        return None

    # Parse the JSON data from the response
    data = response.json()

    # Check if the 'lowest_price' field is present in the data
    try:
        lowest_price = data["lowest_price"]
    except KeyError:
        lowest_price = None

    # Return the lowest price (or None if there is no price information)
    return lowest_price

def get_all_items():
    # Define a list of all items
    all_items = [
        "AK-47 | Slate (Factory New)",
        "USP-S | Ticket to Hell (Factory New)",
        "M4A1-S | Printstream (Factory New)",
        "Desert Eagle | Night Heist (Factory New)",
        "Desert Eagle | Trigger Discipline (Factory New)",
        "SSG 08 | Fever Dream (Factory New)"
    ]

    # Return the list of all items
    return all_items

def get_lowest_price_by_item(items):
    # Create an empty dictionary to store the lowest prices for each item
    prices = {}

    # Loop through each item
    for item in items:
        # Get the lowest price for the item
        lowest_price = get_item_price(item)

        # Skip items with no price information
        if lowest_price is None:
            continue

        # Add the item and its lowest price to the prices dictionary
        prices[item] = lowest_price

    # Return the prices dictionary
    return prices

if __name__ == "__main__":
    # Get a list of all items
    all_items = get_all_items()

    # Get the lowest price for each item
    lowest_prices = get_lowest_price_by_item(all_items)

    # Print the lowest price for each item
    for item, price in lowest_prices.items():
        print(f"{item}: {price}")
