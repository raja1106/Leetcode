class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.arr = [-1] * k
        self.size = 0
        self.front = 0          # index of current front element (valid when size > 0)
        self.rear = -1          # index of current rear element (valid when size > 0)

    def insertFront(self, value: int) -> bool:
        if self.size == self.k:
            return False

        if self.size == 0:
            # first element: front and rear both point to it
            self.front = 0
            self.rear = 0
            self.arr[self.front] = value
        else:
            # move front backward circularly, then write
            self.front = (self.front - 1 + self.k) % self.k
            self.arr[self.front] = value

        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.k:
            return False

        if self.size == 0:
            self.front = 0
            self.rear = 0
            self.arr[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.k
            self.arr[self.rear] = value

        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False

        # optional: clear slot
        # self.arr[self.front] = -1

        if self.size == 1:
            # becomes empty
            self.size = 0
            self.front = 0
            self.rear = -1
            return True

        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False

        # optional: clear slot
        # self.arr[self.rear] = -1

        if self.size == 1:
            self.size = 0
            self.front = 0
            self.rear = -1
            return True

        self.rear = (self.rear - 1 + self.k) % self.k
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.size == 0:
            return -1
        return self.arr[self.front]

    def getRear(self) -> int:
        if self.size == 0:
            return -1
        return self.arr[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# ---------- quick sanity tests ----------
if __name__ == "__main__":
    d = MyCircularDeque(3)
    assert d.insertLast(1) is True     # [1]
    assert d.insertLast(2) is True     # [1,2]
    assert d.insertFront(3) is True    # [3,1,2]
    assert d.insertFront(4) is False   # full
    assert d.getRear() == 2
    assert d.isFull() is True
    assert d.deleteLast() is True      # [3,1]
    assert d.insertFront(4) is True    # [4,3,1]
    assert d.getFront() == 4
    assert d.deleteFront() is True     # [3,1]
    assert d.getFront() == 3
    assert d.deleteFront() is True     # [1]
    assert d.deleteFront() is True     # []
    assert d.deleteFront() is False
    assert d.getFront() == -1
    print("All tests passed!")