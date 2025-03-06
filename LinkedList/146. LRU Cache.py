class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Create dummy head and tail nodes.
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node: Node):
        """Always add the new node right after the head."""
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: Node):
        """Remove an existing node from the linked list."""
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node: Node):
        """Move an existing node to the head (most recently used)."""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> Node:
        """Pop the last node (least recently used)."""
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1

        # Move the accessed node to the head (most recently used).
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if node:
            # Update the value.
            node.value = value
            self._move_to_head(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)

            if len(self.cache) > self.capacity:
                # Pop the tail and remove its key from the cache.
                tail_node = self._pop_tail()
                del self.cache[tail_node.key]


# Example usage:
if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))  # returns 1
    lru.put(3, 3)  # evicts key 2
    print(lru.get(2))  # returns -1 (not found)
    lru.put(4, 4)  # evicts key 1
    print(lru.get(1))  # returns -1 (not found)
    print(lru.get(3))  # returns 3
    print(lru.get(4))  # returns 4
