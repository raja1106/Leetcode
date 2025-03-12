class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.freq = 1  # initial frequency
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """A helper data structure to maintain a doubly linked list of nodes."""

    def __init__(self):
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node: Node):
        """Always add new nodes right after head (most recently used in this frequency)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node: Node):
        """Remove an existing node."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def pop_tail(self) -> Node:
        """Pop the node right before the tail (least recently used in this frequency)."""
        if self.tail.prev == self.head:
            return None  # list is empty
        node = self.tail.prev
        self.remove_node(node)
        return node

    def is_empty(self) -> bool:
        return self.head.next == self.tail


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_table = {}  # key -> Node
        self.freq_table = {}  # freq -> DoublyLinkedList

    def _update_node(self, node: Node):
        """Helper function to update a node's frequency."""
        freq = node.freq
        self.freq_table[freq].remove_node(node)

        # If the current list is empty and freq was the minimum frequency, update min_freq
        if freq == self.min_freq and self.freq_table[freq].is_empty():
            self.min_freq += 1

        # Increase the node's frequency
        node.freq += 1
        new_freq = node.freq

        # Add the node to the list corresponding to the new frequency
        if new_freq not in self.freq_table:
            self.freq_table[new_freq] = DoublyLinkedList()
        self.freq_table[new_freq].add_node(node)

    def get(self, key: int) -> int:
        if key not in self.key_table:
            return -1

        node = self.key_table[key]
        self._update_node(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_table:
            # Update the value and frequency.
            node = self.key_table[key]
            node.value = value
            self._update_node(node)
        else:
            if self.size == self.capacity:
                # Evict the least frequently used node
                # The least frequently used nodes are in freq_table[min_freq]
                list_to_evict = self.freq_table[self.min_freq]
                node_to_evict = list_to_evict.pop_tail()
                if node_to_evict:
                    del self.key_table[node_to_evict.key]
                    self.size -= 1

            # Insert the new node
            new_node = Node(key, value)
            self.key_table[key] = new_node
            # New node always has a frequency of 1.
            if 1 not in self.freq_table:
                self.freq_table[1] = DoublyLinkedList()
            self.freq_table[1].add_node(new_node)
            self.min_freq = 1  # reset min_freq to 1
            self.size += 1


# Example usage:
if __name__ == "__main__":
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    print(lfu.get(1))  # returns 1
    lfu.put(3, 3)  # evicts key 2 since key 1 has higher frequency now
    print(lfu.get(2))  # returns -1 (not found)
    print(lfu.get(3))  # returns 3
    lfu.put(4, 4)  # evicts key 1 or 3 based on frequency and recency
    print(lfu.get(1))  # returns -1 or valid value based on internal state
    print(lfu.get(3))  # returns value if not evicted
    print(lfu.get(4))  # returns 4
