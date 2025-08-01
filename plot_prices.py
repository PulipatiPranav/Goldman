import matplotlib.pyplot as plt
from data_loader import get_stock_data

def plot_price(ticker):
    df = get_stock_data(ticker, '2015-01-01', '2024-01-01')
    plt.figure(figsize=(14, 7))
    plt.plot(df['Date'], df['Close'], label='Close Price')
    plt.title(f'{ticker} Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_price('AAPL')
