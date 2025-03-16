import collections
import unittest


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

class CircularMovingAverage:
    def __init__(self, size: int):
        if size <= 0:
            raise ValueError("Window size must be positive.")
        self.size = size  # Fixed window size (capacity)
        self.buffer = [0] * size  # Pre-allocate buffer with default values
        self.index = 0  # Pointer to the next insertion position
        self.count = 0  # Number of values inserted (up to size)
        self.window_sum = 0  # Running sum of current window elements

    def next(self, val: int) -> float:
        """
        Adds a new value to the circular buffer and returns the current moving average.
        """
        # If buffer is not yet full, increase the count
        if self.count < self.size:
            self.count += 1
        else:
            # Buffer is full: subtract the value that is about to be overwritten
            self.window_sum -= self.buffer[self.index]

        # Insert the new value and update the running sum
        self.buffer[self.index] = val
        self.window_sum += val

        # Move the index pointer forward (wrapping around if needed)
        self.index = (self.index + 1) % self.size

        # Return the moving average over the number of elements added so far
        return self.window_sum / self.count


# Helper function to check approximate equality for floats
def approx_equal(a, b, tol=1e-6):
    return abs(a - b) < tol
def run_tests():
    # Test 1: Single Element Window
    print("Test 1: Single Element Window")
    ma = MovingAverage(1)
    result = ma.next(5)
    assert approx_equal(result, 5.0), f"Expected 5.0, got {result}"
    result = ma.next(3)
    assert approx_equal(result, 3.0), f"Expected 3.0, got {result}"
    result = ma.next(10)
    assert approx_equal(result, 10.0), f"Expected 10.0, got {result}"
    print("Test 1 passed.\n")

    # Test 2: Multiple Elements
    print("Test 2: Multiple Elements")
    ma = MovingAverage(3)
    result = ma.next(1)  # window: [1]
    assert approx_equal(result, 1.0), f"Expected 1.0, got {result}"
    result = ma.next(10)  # window: [1, 10] -> average = (1 + 10)/2
    expected = (1 + 10) / 2
    assert approx_equal(result, expected), f"Expected {expected}, got {result}"
    result = ma.next(3)  # window: [1, 10, 3] -> average = (1 + 10 + 3)/3
    expected = (1 + 10 + 3) / 3
    assert approx_equal(result, expected), f"Expected {expected}, got {result}"
    result = ma.next(5)  # window: [10, 3, 5] -> average = (10 + 3 + 5)/3
    expected = (10 + 3 + 5) / 3
    assert approx_equal(result, expected), f"Expected {expected}, got {result}"
    print("Test 2 passed.\n")

    # Test 3: Negative Numbers
    print("Test 3: Negative Numbers")
    ma = MovingAverage(2)
    result = ma.next(-1)  # window: [-1]
    assert approx_equal(result, -1.0), f"Expected -1.0, got {result}"
    result = ma.next(-3)  # window: [-1, -3] -> average = (-1 - 3)/2
    expected = (-1 - 3) / 2
    assert approx_equal(result, expected), f"Expected {expected}, got {result}"
    result = ma.next(4)   # window: [-3, 4] -> average = (-3 + 4)/2
    expected = (-3 + 4) / 2
    assert approx_equal(result, expected), f"Expected {expected}, got {result}"
    print("Test 3 passed.\n")

    # Test 4: Zeros and Positive Numbers
    print("Test 4: Zeros and Positive Numbers")
    ma = MovingAverage(3)
    result = ma.next(0)  # window: [0]
    assert approx_equal(result, 0.0), f"Expected 0.0, got {result}"
    result = ma.next(0)  # window: [0, 0]
    assert approx_equal(result, 0.0), f"Expected 0.0, got {result}"
    result = ma.next(0)  # window: [0, 0, 0]
    assert approx_equal(result, 0.0), f"Expected 0.0, got {result}"
    result = ma.next(10) # window: [0, 0, 10] -> average = (0 + 0 + 10)/3
    expected = (0 + 0 + 10) / 3
    assert approx_equal(result, expected), f"Expected {expected}, got {result}"
    print("Test 4 passed.\n")

    # Test 5: Return Type
    print("Test 5: Return Type")
    ma = MovingAverage(3)
    result = ma.next(1)
    assert isinstance(result, float), f"Expected type float, got {type(result)}"
    print("Test 5 passed.\n")

    # Test 6: Continued Moving Average
    print("Test 6: Continued Moving Average")
    ma = MovingAverage(4)
    inputs = [2, 4, 6, 8, 10]
    expected_values = [
        2.0,                   # window: [2]
        (2 + 4) / 2,           # window: [2, 4]
        (2 + 4 + 6) / 3,       # window: [2, 4, 6]
        (2 + 4 + 6 + 8) / 4,   # window: [2, 4, 6, 8]
        (4 + 6 + 8 + 10) / 4   # window: [4, 6, 8, 10] because 2 is removed
    ]
    for i, (inp, expected) in enumerate(zip(inputs, expected_values)):
        result = ma.next(inp)
        assert approx_equal(result, expected), f"Step {i}: expected {expected}, got {result}"
    print("Test 6 passed.\n")

    print("All tests passed successfully!")

if __name__ == "__main__":
    run_tests()