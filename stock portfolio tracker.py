print("📈 Welcome to Rejoice's Stock Portfolio Tracker!")

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 180,
    "MSFT": 420
}

stock = input("Enter stock symbol: ").upper()

if stock in stocks:
    quantity = int(input("Enter quantity: "))

    price = stocks[stock]
    total = price * quantity

    print("Stock:", stock)
    print("Price per share:", price)
    print("Quantity:", quantity)
    print("Total investment:", total)

    with open("portfolio.csv", "w") as file:
        file.write("Stock,Price,Quantity,Total\n")
        file.write(f"{stock},{price},{quantity},{total}\n")

    print("Record saved to portfolio.csv")

else:
    print("Sorry, that stock is not available.")