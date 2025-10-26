from collections import deque
from typing import List

from collections import deque


class Solution_Oct_2025:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        result = []
        for i in range(k):
            while window and window[-1] < nums[i]:
                window.pop()
            window.append(nums[i])
        result.append(window[0])

        for i in range(k, len(nums)):
            if nums[i - k] == window[0]:
                window.popleft()
            while window and window[-1] < nums[i]:
                window.pop()
            window.append(nums[i])
            result.append(window[0])

        return result


class Solution:
    def maxSlidingWindow(self, nums: List[int], window_size: int) -> List[int]:
        def maintain_monotonic_deque(monotonic_deque: deque, value: int):
            """Maintains a decreasing order in the deque by removing smaller elements."""
            while monotonic_deque and monotonic_deque[-1] < value:
                monotonic_deque.pop()
            monotonic_deque.append(value)

        max_values = []  # Stores the maximum values for each window
        monotonic_deque = deque()  # Monotonic deque to maintain max elements in decreasing order

        # Initialize the first window
        for i in range(window_size):
            maintain_monotonic_deque(monotonic_deque, nums[i])

        max_values.append(monotonic_deque[0])  # Store max of first window

        # Slide the window across the array
        for i in range(window_size, len(nums)):
            if monotonic_deque[0] == nums[i - window_size]:
                monotonic_deque.popleft()  # Remove the element that goes out of the window

            maintain_monotonic_deque(monotonic_deque, nums[i])  # Insert new element maintaining order
            max_values.append(monotonic_deque[0])  # Store max for the current window

        return max_values


from collections import deque
from typing import List


class Solution_Using_index:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = deque()  # Stores indices, not values

        # Initialize first window
        for i in range(k):
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            window.append(i)
        result.append(nums[window[0]])

        # Process remaining elements
        for i in range(k, len(nums)):
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            window.append(i)

            # Remove elements out of window
            if window[0] == i - k:
                window.popleft()

            result.append(nums[window[0]])

        return result
