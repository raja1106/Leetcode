class Logger:
    def __init__(self):
        # Dictionary stores: { message: last_printed_timestamp }
        self.msg_log = {} # should not use Counter even though Counter works here

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # Check if message is new or 10+ seconds have passed
        if message not in self.msg_log or timestamp >= self.msg_log[message] + 10:
            self.msg_log[message] = timestamp
            return True

        return False


from collections import deque


class Logger_Scalable_Solution:
    def __init__(self):
        # Stores (timestamp, message) in chronological order
        self.queue = deque()
        # Stores only unique messages currently in the 10-second window
        self.msg_set = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # 1. Cleanup: Remove messages from the window that are older than 10s
        while self.queue and timestamp >= self.queue[0][0] + 10:
            old_time, old_msg = self.queue.popleft()
            self.msg_set.remove(old_msg)

        # 2. Check: If the message is in our current window, don't print
        if message in self.msg_set:
            return False

        # 3. Action: Add new message to the queue and set
        self.queue.append((timestamp, message))
        self.msg_set.add(message)
        return True


import threading
from collections import deque


class Logger_MultiThreading:
    def __init__(self):
        self.queue = deque()
        self.msg_set = set()
        # The Lock acts as a "talking stick"
        self.lock = threading.Lock()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # 'with self.lock' ensures the lock is released even if an error occurs
        with self.lock:
            # 1. Cleanup
            while self.queue and timestamp >= self.queue[0][0] + 10:
                old_time, old_msg = self.queue.popleft()
                self.msg_set.discard(old_msg)  # Use discard to avoid KeyError

            # 2. Check
            if message in self.msg_set:
                return False

            # 3. Action
            self.queue.append((timestamp, message))
            self.msg_set.add(message)
            return True


import threading
from collections import deque


class LoggerBucket:
    """A mini-logger that handles its own locking and storage."""

    def __init__(self):
        self.lock = threading.Lock()
        self.queue = deque()
        self.msg_set = set()

    def should_print(self, timestamp: int, message: str) -> bool:
        with self.lock:
            # 1. Cleanup
            while self.queue and timestamp >= self.queue[0][0] + 10:
                _, old_msg = self.queue.popleft()
                self.msg_set.discard(old_msg)

            # 2. Check & Action
            if message in self.msg_set:
                return False

            self.queue.append((timestamp, message))
            self.msg_set.add(message)
            return True


class HighPerformanceLogger:
    def __init__(self, num_buckets: int = 16):
        # Create multiple independent buckets
        self.num_buckets = num_buckets
        self.buckets = [LoggerBucket() for _ in range(num_buckets)]

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # Use hash to determine which bucket this message belongs to
        bucket_index = hash(message) % self.num_buckets
        return self.buckets[bucket_index].should_print(timestamp, message)