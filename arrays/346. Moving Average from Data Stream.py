import collections


class MovingAverage:

    def __init__(self, size: int):
        self.window = collections.deque()
        self.window_size = size
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.window_sum += val
        self.window.append(val)

        if len(self.window) > self.window_size:
            self.window_sum -= self.window.popleft()

        return float(self.window_sum) / len(self.window)
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
