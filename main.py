# CodeAlpha Internship - Task 2
# Stock Portfolio Tracker

def main():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOG": 150,
        "MSFT": 420,
        "AMZN": 180
    }

    portfolio = []

    print("================================")
    print("     STOCK PORTFOLIO TRACKER    ")
    print("================================\n")

    print("Available Stocks:")
    for stock, price in stock_prices.items():
        print(f"{stock} - ${price}")
    print()

    while True:
        stock = input("Enter stock symbol: ").strip().upper()

        if stock not in stock_prices:
            print("Stock not available. Please choose from the list.\n")
            continue

        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than 0.\n")
                    continue

                break

            except ValueError:
                print("Please enter a valid number.\n")

        price = stock_prices[stock]
        investment = price * quantity

        portfolio.append((stock, quantity, price, investment))

        print(f"\n{stock}: {quantity} \u00d7 ${price} = ${investment}\n")

        choice = input("Add another stock? (y/n): ").strip().lower()
        print()

        if choice != "y":
            break

    total_investment = sum(item[3] for item in portfolio)

    print("================================")
    print("        PORTFOLIO SUMMARY       ")
    print("================================\n")

    for stock, quantity, price, investment in portfolio:
        print(f"{stock}: {quantity} \u00d7 ${price} = ${investment}")

    print("--------------------------------")
    print(f"Total Investment: ${total_investment}")
    print("================================\n")

    with open("portfolio.txt", "w", encoding="utf-8") as file:
        file.write("STOCK PORTFOLIO\n")
        file.write("==============================\n\n")

        for stock, quantity, price, investment in portfolio:
            file.write(f"{stock}: {quantity} \u00d7 ${price} = ${investment}\n")

        file.write(f"\nTotal Investment: ${total_investment}\n")

    print("Portfolio saved to portfolio.txt")


if __name__ == "__main__":
    main()
