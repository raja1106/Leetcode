from collections import deque

class PhoneDirectory_using_array_for_check:
    """
    Free numbers are stored in a queue (FIFO) or stack (LIFO).
    We use a boolean array `is_free` for O(1) check() and to prevent double-release duplicates.
    """

    def __init__(self, maxNumbers: int):
        self.max = maxNumbers
        self.free = deque(range(maxNumbers))     # queue of available numbers
        self.is_free = [True] * maxNumbers       # True => available, False => assigned

    def get(self) -> int:
        # Pop until we find a truly-free number (handles any stale entries if ever present)
        while self.free:
            num = self.free.popleft()
            if self.is_free[num]:
                self.is_free[num] = False
                return num
        return -1

    def check(self, number: int) -> bool:
        if number < 0 or number >= self.max:
            return False
        return self.is_free[number]

    def release(self, number: int) -> None:
        if number < 0 or number >= self.max:
            return
        # Only release if it was assigned; prevents double-release duplicates.
        if not self.is_free[number]:
            self.is_free[number] = True
            self.free.append(number)



class PhoneDirectory_Using_Set:
    def __init__(self, maxNumbers: int):
        # Queue to maintain the order of available numbers
        self.queue = deque(range(maxNumbers))
        # Set for O(1) membership checks
        self.available_set = set(range(maxNumbers))
        self.max_val = maxNumbers

    def get(self) -> int:
        """Provides an available number or -1 if empty."""
        if not self.queue:
            return -1

        # Pull from the front of the queue
        num = self.queue.popleft()
        # Remove from set so check() returns False
        self.available_set.remove(num)
        return num

    def check(self, number: int) -> bool:
        """Returns True if the number is available."""
        # Simple O(1) set lookup
        return number in self.available_set

    def release(self, number: int) -> None:
        """Releases a number back into the pool."""
        # Edge case: Don't release if it's already available or out of bounds
        if number < 0 or number >= self.max_val or number in self.available_set:
            return

        # Add back to both structures
        self.available_set.add(number)
        self.queue.append(number)



class PhoneDirectory_MY_Solution:
    """
     - - -
     T means avaiable, not booked
     F means Not available
    """

    def __init__(self, maxNumbers: int):
        self.phone_book = [True] * maxNumbers
        self.number_set = set(list(range(maxNumbers)))

    def get(self) -> int:
        if self.number_set:
            initial_element = self.number_set.pop()
            self.phone_book[initial_element] = False
            return initial_element
        return -1

    def check(self, number: int) -> bool:
        if number >= len(self.phone_book):
            return False
        return self.phone_book[number]

    def release(self, number: int) -> None:
        self.phone_book[number] = True
        self.number_set.add(number)
