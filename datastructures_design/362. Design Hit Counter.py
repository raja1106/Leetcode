from collections import deque


class HitCounter:

    def __init__(self):
        self.window = deque()

    def hit(self, timestamp: int) -> None:
        self.window.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.window and self.window[0] <= timestamp - 300:
            self.window.popleft()

        return len(self.window)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

class HitCounter_Scalable:
    def __init__(self):
        # Stores [timestamp, hit_count]
        self.window = deque()
        self.total_hits = 0

    def hit(self, timestamp: int) -> None:
        # If the hit is at the same timestamp as the last one, just increment count
        if self.window and self.window[-1][0] == timestamp:
            self.window[-1][1] += 1
        else:
            self.window.append([timestamp, 1])

        self.total_hits += 1

    def getHits(self, timestamp: int) -> int:
        # Remove hits older than 300 seconds
        while self.window and self.window[0][0] <= timestamp - 300:
            _, count = self.window.popleft()
            self.total_hits -= count

        return self.total_hits


class HitCounter_Scalable_Memory_Optimized:
    def __init__(self):
        self.size = 300
        self.hits = [0] * self.size
        self.times = [0] * self.size
        self.total_hits = 0

    def _cleanup(self, timestamp: int):
        """Internal helper to remove old data and update the total."""
        for i in range(self.size):
            # If the bucket is older than 300s but still has hit counts
            if timestamp - self.times[i] >= 300 and self.hits[i] > 0:
                self.total_hits -= self.hits[i]
                self.hits[i] = 0
                # We don't necessarily need to reset self.times[i] here,
                # but we must zero the hits.

    def hit(self, timestamp: int) -> None:
        index = timestamp % self.size

        # If this bucket is from a previous cycle, subtract its old hits from total
        if self.times[index] != timestamp:
            self.total_hits -= self.hits[index]
            self.times[index] = timestamp
            self.hits[index] = 1
        else:
            self.hits[index] += 1

        self.total_hits += 1

    def getHits(self, timestamp: int) -> int:
        # Before returning, ensure we subtract hits that just expired
        self._cleanup(timestamp)
        return self.total_hits