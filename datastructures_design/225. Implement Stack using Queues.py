from collections import deque


class MyStack:
    def __init__(self):
        # Use a real deque to ensure O(1) removals from the front
        self.queue = deque()

    def push(self, x: int) -> None:
        # 1. Add the new element to the back
        self.queue.append(x)

        # 2. Rotate the queue: move all previous elements to the back
        # This makes the new element the "head" of the queue
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        # Now we can just use popleft() which is O(1)
        return self.queue.popleft() if self.queue else -1

    def top(self) -> int:
        return self.queue[0] if self.queue else -1

    def empty(self) -> bool:
        return not self.queue


class MyStack_using_arraylist:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if not self.queue:
            return -1
        return self.queue.pop()

    def top(self) -> int:
        if not self.queue:
            return -1
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0

