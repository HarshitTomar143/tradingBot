class TrendStrategy:
    def __init__(self):
        self.prices = []

    def decide(self, current_price):
        self.prices.append(current_price)

        if len(self.prices) < 3:
            return "hold"

        if self.prices[-1] > self.prices[-2] > self.prices[-3]:
            return "buy"

        if self.prices[-1] < self.prices[-2] < self.prices[-3]:
            return "sell"

        return "hold"
