class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev


class AllOne:
    def __init__(self):
        self.mapping = {}  # key -> Node
        self.head = Node(0)  # Sentinel (Min side)
        self.tail = Node(0)  # Sentinel (Max side)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert_after(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def inc(self, key: str) -> None:
        if key not in self.mapping:
            # Case 1: Key is new, needs to go into a Node with count 1
            if self.head.next.count != 1:
                self._insert_after(self.head, Node(1))
            self.head.next.keys.add(key)
            self.mapping[key] = self.head.next
        else:
            # Case 2: Key exists, move to current_count + 1
            cur_node = self.mapping[key]
            if cur_node.next.count != cur_node.count + 1:
                self._insert_after(cur_node, Node(cur_node.count + 1))

            cur_node.next.keys.add(key)
            self.mapping[key] = cur_node.next
            cur_node.keys.remove(key)
            if not cur_node.keys:
                cur_node.remove()

    def dec(self, key: str) -> None:
        if key not in self.mapping:
            return

        cur_node = self.mapping[key]
        cur_node.keys.remove(key)

        if cur_node.count > 1:
            if cur_node.prev.count != cur_node.count - 1:
                # Need to insert a node for the decremented count
                new_node = Node(cur_node.count - 1)
                self._insert_after(cur_node.prev, new_node)

            cur_node.prev.keys.add(key)
            self.mapping[key] = cur_node.prev
        else:
            # count becomes 0, just remove from mapping
            del self.mapping[key]

        if not cur_node.keys:
            cur_node.remove()

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        # Set iteration is O(1) for getting the first element
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))