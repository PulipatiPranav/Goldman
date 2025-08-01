import yfinance as yf
import pandas as pd
import os

def fetch_stock_data(ticker: str, start_date: str, end_date: str, interval: str ='1d'):

    """
    Fetch historical stock data for a given ticker symbol between specified dates.

    Parameters:
    ticker (str): The stock ticker symbol.
    start_date (str): The start date in 'YYYY-MM-DD' format.
    end_date (str): The end date in 'YYYY-MM-DD' format.

    Returns:
    pd.DataFrame: A DataFrame containing the stock data.
    """
    print(f"Fetching data for {ticker} from {start_date} to {end_date} with interval {interval}")
    data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
    if data.empty:
        print(f"No data found for {ticker} in the specified date range.")
        return
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join('data', f'{ticker}_{interval}.csv')
    data.to_csv(file_path, index=True)
    print(f"Data saved to {file_path}")


    

if __name__ == "__main__":
    ticker = 'AAPL'
    start_date = '2015-01-01'
    end_date = '2024-01-01'
    fetch_stock_data(ticker, start_date, end_date)