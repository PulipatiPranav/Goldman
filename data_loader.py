import yfinance as yf
import pandas as pd

def get_stock_data(ticker, start_date, end_date):
    """
    Fetch historical stock data for a given ticker symbol between specified dates.

    Parameters:
    ticker (str): The stock ticker symbol.
    start_date (str): The start date in 'YYYY-MM-DD' format.
    end_date (str): The end date in 'YYYY-MM-DD' format.

    Returns:
    pd.DataFrame: A DataFrame containing the stock data.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    data.dropna(inplace=True)  # Drop rows with missing values
    data.reset_index(inplace=True)  # Reset index to have a clean DataFrame

    return data

if __name__ == "__main__":
    df = get_stock_data('AAPL', '2015-01-01', '2024-01-01')
    print(df.head())
