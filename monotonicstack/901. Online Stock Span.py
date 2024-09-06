class StockSpanner:

    def __init__(self):
        self.st = []  # (price, span)

    def next(self, price: int) -> int:
        value=1
        while(self.st and self.st[-1][0] < price):
            value=value+self.st[-1][1]
            self.st.pop()
        self.st.append(price,value)