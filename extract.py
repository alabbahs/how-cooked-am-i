import requests
import os
import json
from dotenv import load_dotenv
from rich import print

load_dotenv()

base_url = "https://www.alphavantage.co/query"
api_key = os.getenv("API_KEY")

symbols = ["AAPL", "TSLA", "AMZN", "GOOGL",
           "MSFT", "NFLX", "NVDA", "FB", "BABA", "JPM"]


def get_data() -> dict:
    stock_data = {}

    for symbol in symbols:
        url = f"{base_url}?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            stock_data[symbol] = response.json()
        else:
            print(f"Failed to fetch data for {symbol}: {response.status_code}")

    return stock_data


def create_json(data : dict) -> None:
    if not os.path.exists("data"):
        os.makedirs("data")
        print("Data folder has been created")

    with open("data/stock_symbols.json", "w") as file:
        file.write(json.dumps(data, indent=4))
    
    print("Json file has been created in data directory")


if __name__ == "__main__":
    data = get_data()
    create_json(data)
