from collections import Counter, defaultdict

class FreqStack:
    def __init__(self):
        self.frequency_map = Counter()              # val -> frequency
        self.freq_buckets = defaultdict(list)     # freq -> stack of vals (recency)
        self.max_frequency = 0

    def push(self, val: int) -> None:
        new_freq = self.frequency_map[val] + 1
        self.frequency_map[val] = new_freq
        self.freq_buckets[new_freq].append(val)
        if new_freq > self.max_frequency:
            self.max_frequency = new_freq

    def pop(self) -> int:
        if self.max_frequency == 0:
            raise IndexError("FreqStack is empty")

        val = self.freq_buckets[self.max_frequency].pop()
        self.frequency_map[val] -= 1

        if not self.freq_buckets[self.max_frequency]:
            self.max_frequency -= 1
        return val



from collections import defaultdict
from heapq import heappush, heappop

class FreqStack_Using_Heap:
    """
    A stack-like data structure that pops the most frequently occurring element.
    When multiple elements have the same frequency, the most recently pushed element is popped.
    """

    def __init__(self):
        """Initialize the frequency stack with necessary data structures."""
        # Dictionary to track the frequency count of each element
        self.frequency_count = defaultdict(int)

        # Min heap (priority queue) to maintain elements by frequency and recency
        # Stored as tuples: (-frequency, -timestamp, value)
        # Negative values used to simulate max heap behavior
        self.priority_queue = []

        # Timestamp counter to track insertion order
        self.timestamp = 0

    def push(self, val: int) -> None:
        """
        Push an element onto the frequency stack.

        Args:
            val: The integer value to push onto the stack
        """
        # Increment timestamp for this operation
        self.timestamp += 1

        # Update frequency count for this value
        self.frequency_count[val] += 1

        # Add to priority queue with negative frequency and timestamp for max heap behavior
        # Priority order: highest frequency first, then most recent timestamp
        heappush(self.priority_queue,
                 (-self.frequency_count[val], -self.timestamp, val))

    def pop(self) -> int:
        """
        Pop and return the most frequent element from the stack.
        If there's a tie in frequency, return the most recently pushed element.

        Returns:
            The popped integer value
        """
        # Extract the value with highest priority (most frequent, most recent)
        _, _, value = heappop(self.priority_queue)

        # Decrease the frequency count for this value
        self.frequency_count[value] -= 1

        return value


def test_freq_stack():
    print("=== Test Case 1: Basic push/pop ===")
    fs = FreqStack()
    fs.push(5)
    fs.push(7)
    fs.push(5)
    fs.push(7)
    fs.push(4)
    fs.push(5)

    print(fs.pop())  # Expected 5 (freq 3)
    print(fs.pop())  # Expected 7 (freq 2, most recent)
    print(fs.pop())  # Expected 5
    print(fs.pop())  # Expected 4

    print("\n=== Test Case 2: Single element ===")
    fs = FreqStack()
    fs.push(10)
    print(fs.pop())  # Expected 10

    print("\n=== Test Case 3: Multiple same values ===")
    fs = FreqStack()
    fs.push(1)
    fs.push(1)
    fs.push(1)
    print(fs.pop())  # 1
    print(fs.pop())  # 1
    print(fs.pop())  # 1

    print("\n=== Test Case 4: Interleaved values ===")
    fs = FreqStack()
    fs.push(1)
    fs.push(2)
    fs.push(3)
    fs.push(2)
    fs.push(1)
    fs.push(2)

    # freq(2)=3, freq(1)=2, freq(3)=1
    print(fs.pop())  # 2
    print(fs.pop())  # 1
    print(fs.pop())  # 2
    print(fs.pop())  # 3
    print(fs.pop())  # 1
    print(fs.pop())  # 2

    print("\n=== Test Case 5: Error case ===")
    fs = FreqStack()
    try:
        fs.pop()
    except IndexError as e:
        print("Caught expected exception:", e)


if __name__ == "__main__":
    test_freq_stack()