import yfinance as yf
import json
import os

def fetch_stock_data(ticker, period='1y', interval='1d'):
    # Fetch data from Yahoo Finance
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)

    # Prepare the data in the format needed for D3.js
    data = []
    for index, row in hist.iterrows():
        data.append({
            'date': index.strftime('%Y-%m-%d'),
            'open': row['Open'],
            'high': row['High'],
            'low': row['Low'],
            'close': row['Close']
        })

    # Save data to a JSON file
    filename = f"{ticker.lower()}_data.json"
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data for {ticker} saved to {filename}")

if __name__ == "__main__":
    # Define the tickers for which data should be fetched
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "NVDA", "BRK.B", "JNJ", "V"]
    
    # Fetch data for each ticker
    for ticker in tickers:
        fetch_stock_data(ticker)
