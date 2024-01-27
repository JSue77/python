import yfinance

netflix = yfinance.Ticker('NFLX')
netflix_info = netflix.info
print(netflix_info['regularMarketPrice'])