class Allocator:
    def __init__(self, n: int):
        self.mem = [0] * n
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        count = 0
        for i in range(self.n):
            if self.mem[i] == 0:
                count += 1
                if count == size:
                    start = i - size + 1
                    for j in range(start, i + 1):
                        self.mem[j] = mID
                    return start
            else:
                count = 0
        return -1

    def freeMemory(self, mID: int) -> int:
        freed = 0
        for i in range(self.n):
            if self.mem[i] == mID:
                self.mem[i] = 0
                freed += 1
        return freed


class Allocator_using_while:

    def __init__(self, n: int):
        self.arr = [None] * n
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        i = 0

        while i < self.n:
            # Skip allocated blocks
            if self.arr[i] is not None:
                i += 1
                continue

            j = i

            # Find contiguous free block
            while j < self.n and self.arr[j] is None and (j - i) < size:
                j += 1

            # If block found
            if j - i == size:
                for k in range(i, j):
                    self.arr[k] = mID
                return i

            # Jump to failure point (important optimization)
            i = j + 1

        return -1

    def freeMemory(self, mID: int) -> int:
        count = 0

        for i in range(self.n):
            if self.arr[i] == mID:
                self.arr[i] = None
                count += 1

        return count