class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        # Initialize head and tail pointers as dummy nodes
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # Helper function to remove a node from the linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # Helper function to insert a node at the tail (most recently used)
    # Insert the new node just before the dummy tail node
    def insert(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the accessed node to the tail (most recently used)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If the key exists, remove the old node
            self.remove(self.cache[key])
        else:
            # If adding a new key and the cache is full, remove the least recently used (head.next)
            if len(self.cache) >= self.cap:
                lru = self.head.next
                self.remove(lru)
                del self.cache[lru.key]

        # Insert the new key-value pair
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)
