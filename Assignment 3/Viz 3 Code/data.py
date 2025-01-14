import yfinance as yf
import json

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "NVDA", "BRK-B", "JNJ", "V"]

for ticker in tickers:
    stock = yf.Ticker(ticker)
    data = stock.history(period="10y")  # Fetch data for the past 10 years
    data.reset_index(inplace=True)

    market_data = []
    for _, row in data.iterrows():
        market_valuation = row['Close'] * stock.info['sharesOutstanding']  # Estimate market valuation
        market_data.append({
            "date": row['Date'].strftime('%Y-%m-%d'),
            "market_valuation": market_valuation
        })

    filename = f"{ticker.lower().replace('.', '_').replace('-', '_')}_data.json"
    with open(filename, "w") as f:
        json.dump(market_data, f)

print("Data fetched successfully.")
