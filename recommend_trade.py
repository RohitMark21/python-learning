import yfinance as yf

DECISION_BUY = "BUY"
DECISION_HOLD = "HOLD"
DECISION_SELL ="SELL"

def calculate_share_count(budget, live_price):
    return round(budget/live_price, 2)

def get_recommendation(live_price, historical_price, historical_date):
    price_change = round(live_price-historical_price, 2)
    gain=round(price_change/historical_price*100, 2)
    print(f"---> Price change since {historical_date}:",price_change,"USD")
    print("---> Stock has moved by: ",gain,"%")
    if price_change < 0:
        print("---> Recommendation:", DECISION_BUY)
        try:
            budget = float(input("---> What's your budget?\n"))
        except ValueError:
            print("Please enter a number in USD.\n")
            return
        print("---> You can buy", calculate_share_count(budget, live_price), "shares and average down.")
    elif price_change == 0:
        print("---> Recommendation:", DECISION_HOLD)
        print("---> Price is unchanged. Wait for movement or hold what you have.")
    else:
        print("---> Recommended:", DECISION_SELL)
        print("---> You can gain", price_change, "USD per share right now.")

def main():
    print("\n----------TRADE RECOMMENDATIONS FOR NASDAQ (USD)----------")
    valid_company = True
    company = input("Which company do you want recommendations on?\n")
    while True:
        try:
            historical_date = input("When did you invest? (YYYY-MM-DD)\n")
            break;
        except ValueError:
            print("Please enter a number.\n")
    while True:
        try:
            stock = yf.Ticker(yf.Search(company).quotes[0]["symbol"])
            break;
        except:
            print("Company could not be identified. Try a different name.")
    historical_price = stock.history(period="5y")["Close"].loc[:historical_date].iloc[-1]
    live_price = stock.fast_info["last_price"]
    get_recommendation(live_price, historical_price, historical_date)

if __name__ == "__main__":
    main()
