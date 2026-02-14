class Portfolio:
    def __init__(self, initial_balance=1000):
        self.balance = initial_balance
        self.btc = 0
        self.trades = 0

    def buy(self, price):
        if self.balance > 0:
            self.btc = self.balance / price
            self.balance = 0
            self.trades += 1
            print("✅ Bought BTC")

    def sell(self, price):
        if self.btc > 0:
            self.balance = self.btc * price
            self.btc = 0
            self.trades += 1
            print("🔴 Sold BTC")

    def net_worth(self, price):
        return self.balance + (self.btc * price)
