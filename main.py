import time
from price_feed import get_price
from portfolio import Portfolio
from strategy import TrendStrategy

portfolio = Portfolio()
strategy = TrendStrategy()

print("🚀 Trend Bot Started...")

while True:
    try:
        price = get_price()
        decision = strategy.decide(price)

        print(f"Current Price: {price}")

        if decision == "buy":
            portfolio.buy(price)

        elif decision == "sell":
            portfolio.sell(price)

        net = portfolio.net_worth(price)

        print(f"💰 Net Worth: {net:.2f}")
        print(f"📊 Trades: {portfolio.trades}")
        print("-" * 40)

        time.sleep(5)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
