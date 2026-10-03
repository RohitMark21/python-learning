DECISION_BUY = "BUY"
DECISION_HOLD = "HOLD"
DECISION_SELL ="SELL"

def get_recommendation(live_price, historical_price):
    price_change = round(live_price-historical_price, 2)
    gain=round(price_change/historical_price*100, 2)

    if price_change<0:
        return DECISION_BUY, price_change, gain
    elif price_change==0:
        return DECISION_HOLD, price_change, gain
    else:
        return DECISION_SELL, price_change, gain
 