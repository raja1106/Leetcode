class MyHashMap:
    def __init__(self):
        self.SIZE = 10007  # Prime number for better distribution
        self.buckets = [[] for _ in range(self.SIZE)]

    def _hash(self, key):
        return key % self.SIZE  # Hash function

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update value
                return
        bucket.append((key, value))  # Insert new key-value pair

    def get(self, key: int) -> int:
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        return -1  # Not found

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]  # Remove key-value pair
                return
