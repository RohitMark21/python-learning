import yfinance as yf

DECISION_BUY = "BUY"
DECISION_HOLD = "HOLD"
DECISION_SELL ="SELL"

def get_share_count(budget, live_price):
    return round(budget/live_price, 2)

def get_recommendation(live_price, week_ago_price):
    price_change = round(live_price-week_ago_price, 2)
    print("---> Price change in last 7 days:",price_change,"USD")
    if price_change < 0:
        print("---> Recommended:", DECISION_BUY)
        budget = float(input("---> What's your budget?\n"))
        print("---> You can buy", get_share_count(budget, live_price), "shares and average down.")
    elif price_change == 0:
        print("---> Recommended:", DECISION_HOLD)
        print("---> Price is unchanged. Wait for movement or hold what you have.")
    else:
        print("---> Recommended:", DECISION_SELL)
        gain_percentage=price_change/week_ago_price*100
        print("---> You can gain", price_change, "USD (+",round(gain_percentage, 2),"%) per share right now.")

print("----------CURRENCY: USD----------")
company = input("Which company do you want recommendations on?\n")
date_range_in_days = int(input("How many days ago did you invest?\n"))
stock = yf.Ticker(yf.Search(company).quotes[0]["symbol"])
week_ago_price = stock.history(period="5y")["Close"].iloc[-date_range_in_days]
live_price = stock.fast_info["last_price"]
get_recommendation(live_price, week_ago_price)








