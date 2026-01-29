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

class Node:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:
    def __init__(self):
        self.capacity = 16
        self.key_map = [None] * self.capacity
        self.size = 0
        self.load_factor = 0.75

    def _rehash(self) -> None:
        """
        Rehash by *reusing the existing Node objects* (no new node allocations).
        We detach each node from its old chain and prepend it into the new bucket.
        """
        old_map = self.key_map

        self.capacity *= 2
        self.key_map = [None] * self.capacity

        # size remains the same because we are moving nodes, not adding/removing keys
        for head in old_map:
            current = head
            while current:
                nxt = current.next          # save next in old chain
                current.next = None         # detach current node from old list

                new_idx = current.key % self.capacity

                # prepend to new bucket chain (O(1))
                current.next = self.key_map[new_idx]
                self.key_map[new_idx] = current

                current = nxt

    def put(self, key: int, value: int) -> None:
        # rehash check (doesn't change chaining logic; just resizes when needed)
        if (self.size + 1) / self.capacity > self.load_factor:
            self._rehash()

        hash_key = key % self.capacity
        if self.key_map[hash_key] is None:
            self.key_map[hash_key] = Node(key, value)
            self.size += 1
        else:
            head = self.key_map[hash_key]
            current = head
            node_found = False
            prev = None
            while current:
                if current.key == key:
                    current.val = value
                    node_found = True
                    break
                prev = current
                current = current.next

            if not node_found:
                prev.next = Node(key, value)
                self.size += 1

    def get(self, key: int) -> int:
        hash_key = key % self.capacity
        if self.key_map[hash_key] is None:
            return -1

        current = self.key_map[hash_key]
        while current:
            if current.key == key:
                return current.val
            current = current.next

        return -1

    def remove(self, key: int) -> None:
        hash_key = key % self.capacity
        if self.key_map[hash_key] is None:
            return

        head = self.key_map[hash_key]
        if head.key == key:
            self.key_map[hash_key] = head.next
            head.next = None
            self.size -= 1
            return

        current = head
        prev = None
        while current:
            if current.key == key:
                prev.next = current.next
                current.next = None
                self.size -= 1
                return
            prev = current
            current = current.next


# --------- quick tests ----------
if __name__ == "__main__":
    m = MyHashMap()

    # force multiple rehashes
    for i in range(200):
        m.put(i, i * 10)

    assert m.get(0) == 0
    assert m.get(5) == 50
    assert m.get(199) == 1990
    assert m.get(1000) == -1

    m.put(5, 555)
    assert m.get(5) == 555

    m.remove(5)
    assert m.get(5) == -1

    # ensure others still exist
    assert m.get(6) == 60
    assert m.get(150) == 1500

    print("All tests passed!")
