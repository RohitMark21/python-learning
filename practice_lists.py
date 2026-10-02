stocks = ["AAPL", "MSFT", "GOOGL", "NVDA", "TSLA"]
print ("Stock #4: ", stocks[3])
print ("No. of items: ", len(stocks))
for currentitem in stocks:
    print (f"Reading item: {currentitem} ...")
stocksWithA = [currentitem for currentitem in stocks if "a" in currentitem.lower()]
print ("Stocks with \"A\": ", stocksWithA)
