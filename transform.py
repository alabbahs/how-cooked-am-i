import pandas as pd
import json


def flatten_nested_json(data: dict) -> pd.DataFrame:
    """Flattens the nested JSON stock data into a Pandas DataFrame."""
    records = []

    for symbol, details in data.items():
        time_series = details.get("Time Series (5min)", {})
        for timestamp, values in time_series.items():
            record = {
                "symbol": symbol,
                "timestamp": timestamp,
                "open": values["1. open"],
                "high": values["2. high"],
                "low": values["3. low"],
                "close": values["4. close"],
                "volume": values["5. volume"]
            }
            records.append(record)

    return pd.DataFrame(records)


def create_csv(df: pd.DataFrame, filename: str) -> None:
    """Saves the given DataFrame as a CSV file."""
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")


if __name__ == "__main__":
    with open("data/stock_symbols.json", "r") as f:
        data = json.load(f)

    df = flatten_nested_json(data)
    create_csv(df, "data/transformed_stock_data.csv")
