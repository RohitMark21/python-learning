import yfinance as yf

def find_stock(company):
    return yf.Ticker(yf.Search(company).quotes[0]["symbol"]) 

def get_historical_price(stock, historical_date):
    return stock.history(period="5y")["Close"].loc[:historical_date].iloc[-1]

def get_live_price(stock):
    return stock.fast_info["last_price"]
