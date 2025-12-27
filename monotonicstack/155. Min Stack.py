class MinStack_Best:
    def __init__(self):
        self.stack = []  # (val, min_so_far)

    def push(self, val: int) -> None:
        min_so_far = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, min_so_far))

    def pop(self) -> None:
        if not self.stack:
            raise IndexError("pop from empty MinStack")
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            raise IndexError("top from empty MinStack")
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            raise IndexError("getMin from empty MinStack")
        return self.stack[-1][1]

class MinStack_Best_2:

    def __init__(self):
        self.st = []  # (val,min_value)

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append((val, val))
            return
        min_val = self.st[-1][1]
        if self.st[-1][1] > val:
            min_val = val
        self.st.append((val, min_val))

    def pop(self) -> None:
        if self.st:
            self.st.pop()

    def top(self) -> int:
        if self.st:
            return self.st[-1][0]
        else:
            return -1

    def getMin(self) -> int:
        if self.st:
            return self.st[-1][1]
        else:
            return -1


class MinStack_Two_stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.stack:
            top = self.stack.pop()
            if top == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        raise IndexError("Top called on empty stack")

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        raise IndexError("getMin called on empty stack")
