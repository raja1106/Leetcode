import collections


class MovingAverage:

    def __init__(self, size: int):
        self.window = collections.deque()
        self.maxsize = size
        self.totalsofar = 0

    def next(self, val: int) -> float:
        self.totalsofar += val
        self.window.append(val)

        if len(self.window) > self.maxsize:
            self.totalsofar -= self.window.popleft()

        return float(self.totalsofar) / len(self.window)
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
