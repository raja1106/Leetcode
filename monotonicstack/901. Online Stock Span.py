class StockSpanner:

    def __init__(self):
        self.st = []  # Stack to store (day, price)
        self.day = 0  # Start day count at 0

    def next(self, price: int) -> int:
        while self.st and self.st[-1][1] <= price:
            self.st.pop()

        if self.st:
            ans = self.day - self.st[-1][0]
        else:
            ans = self.day + 1  # Span is all days up to the current one

        self.st.append((self.day, price))
        self.day += 1
        return ans
