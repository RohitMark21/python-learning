import stock_data as sd
import recommendations as rec
#---> TEST command: 
#---> python3 trading/recommend_trade.py

def calculate_share_count(budget, live_price):
    return round(budget/live_price, 2)

def recommend_trade(live_price, historical_date, decision, price_change, gain):
    print(f"---> Price change since {historical_date}:",price_change,"USD")
    print("---> Stock has moved by: ",gain,"%")
    print("---> Recommendation:", decision)
    if decision == rec.DECISION_BUY:
        try:
            budget = float(input("---> What's your budget?\n"))
        except ValueError:
            print("Please enter a number in USD.\n")
            return
        print("---> You can buy", calculate_share_count(budget, live_price), "shares and average down.")
    elif decision == rec.DECISION_HOLD:
        print("---> Price is unchanged. Wait for movement or hold what you have.")
    else:
        print("---> You can gain", price_change, "USD per share right now.")

def main():
    print("\n----------TRADE RECOMMENDATIONS FOR NASDAQ (USD)----------")
    company = input("Which company do you want recommendations on?\n")
    historical_date = input("When did you invest? (YYYY-MM-DD)\n")         
    while True:
        try:
            stock = sd.find_stock(company)
            break
        except Exception as e:
            print("Company could not be identified. Try a different name. Exception: \n", e)
            company = input("Re-enter company name:\n")
    historical_price = sd.get_historical_price(stock, historical_date)
    live_price = sd.get_live_price(stock)
    #---> Option 1
    #decision, price_change, gain = rec.get_recommendation(live_price, historical_price)
    #recommend_trade(live_price, historical_date, decision, price_change, gain)
    #---> Option 2
    recommend_trade(live_price, historical_date, *rec.get_recommendation(live_price, historical_price))

if __name__ == "__main__":
    main()
