import yfinance as yf

msft = yf.Ticker("MSFT")
hist = msft.history(period="12mo")

print(hist)