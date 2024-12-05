class ListNode:
    def __init__(self, value=0):
        self.value = value
        self.next = None


class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k  # Maximum size of the queue
        self.size = 0  # Current number of elements in the queue
        self.front = None  # Pointer to the front node of the queue
        self.rear = None  # Pointer to the rear node of the queue

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = ListNode(value)
        if self.isEmpty():
            # First element; initialize front and rear to this new node
            self.front = self.rear = new_node
            self.rear.next = self.front  # Make it circular
        else:
            # Insert new node at the end and update rear pointer
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front  # Maintain circular link

        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        if self.front == self.rear:
            # Only one element in the queue
            self.front = self.rear = None
        else:
            # Remove the front node and update the front pointer
            self.front = self.front.next
            self.rear.next = self.front  # Maintain circular link

        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.front.value

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.rear.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
class MyCircularQueue_Using_Array:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.capacity = k
        self.size = 0
        self.front = 0
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
