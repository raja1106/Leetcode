class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        # This array stores the pending increments
        self.inc = [0] * maxSize

    def push(self, x: int) -> None:
        # Standard O(1) push
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        # Standard O(1) pop with lazy increment application
        idx = len(self.stack) - 1
        if idx < 0:
            return -1

        # 1. Take the increment value for this position
        add_val = self.inc[idx]

        # 2. Pass the increment down to the element below (Lazy Prop)
        if idx > 0:
            self.inc[idx - 1] += add_val

        # 3. Reset the increment at the current top and pop
        self.inc[idx] = 0
        return self.stack.pop() + add_val

    def increment(self, k: int, val: int) -> None:
        # O(1) operation: Only update the last affected index
        # We target the k-th element or the current top of the stack
        idx = min(k, len(self.stack)) - 1
        if idx >= 0:
            self.inc[idx] += val