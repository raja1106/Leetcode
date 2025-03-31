class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next  # Use the provided 'next' if given

    def __repr__(self):
        return f"Node({self.value})"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Maintain a tail pointer for efficient appends
        self.count = 0

    def append(self, node):
        """Append a node at the end of the list."""
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count += 1

    def prepend(self, node):
        """Insert a node at the beginning of the list."""
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.count += 1

    def insert(self, position, node):
        """Insert a node at the specified position."""
        if position < 0 or position > self.count:
            raise IndexError("Position out of bounds")
        if position == 0:
            self.prepend(node)
        elif position == self.count:
            self.append(node)
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            node.next = current.next
            current.next = node
            self.count += 1

    def delete(self, node):
        """Delete the first occurrence of the specified node."""
        current = self.head
        previous = None
        while current:
            if current == node:
                if previous is None:  # Node is at the head
                    self.head = current.next
                    if self.head is None:
                        self.tail = None  # List is now empty
                else:
                    previous.next = current.next
                    if current == self.tail:
                        self.tail = previous
                self.count -= 1
                return  # Only delete the first occurrence
            previous = current
            current = current.next

    def delete_at(self, position):
        """Delete the node at the specified position."""
        if position < 0 or position >= self.count:
            raise IndexError("Position out of bounds")
        if position == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            to_delete = current.next
            current.next = to_delete.next
            if to_delete == self.tail:
                self.tail = current
        self.count -= 1

    def search(self, value):
        """Search for the first node with the specified value.

        Returns:
            The node with the matching value, or None if not found.
        """
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def size(self):
        """Return the number of nodes in the list."""
        return self.count

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next
        return "->".join(nodes)

def run_tests():
    print("Testing append...")
    ll = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    ll.append(node1)
    ll.append(node2)
    ll.append(node3)
    assert ll.head == node1, "Append Test: Head should be node1"
    assert ll.tail == node3, "Append Test: Tail should be node3"
    assert ll.size() == 3, "Append Test: Size should be 3"
    assert repr(ll) == "Node(1)->Node(2)->Node(3)", "Append Test: Incorrect list representation"
    print("Append Test Passed.")

    print("Testing prepend...")
    ll = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    ll.prepend(node1)
    assert ll.head == node1, "Prepend Test: Head should be node1"
    assert ll.tail == node1, "Prepend Test: Tail should be node1"
    ll.prepend(node2)
    assert ll.head == node2, "Prepend Test: Head should be node2 after second prepend"
    assert ll.tail == node1, "Prepend Test: Tail should remain node1"
    assert ll.size() == 2, "Prepend Test: Size should be 2"
    assert repr(ll) == "Node(2)->Node(1)", "Prepend Test: Incorrect list representation"
    print("Prepend Test Passed.")

    print("Testing insert...")
    ll = LinkedList()
    node1 = Node(1)
    node3 = Node(3)
    ll.append(node1)
    ll.append(node3)
    node2 = Node(2)
    ll.insert(1, node2)
    assert repr(ll) == "Node(1)->Node(2)->Node(3)", "Insert Test: Incorrect list representation after middle insertion"
    assert ll.size() == 3, "Insert Test: Size should be 3 after middle insertion"
    # Insert at beginning
    node0 = Node(0)
    ll.insert(0, node0)
    assert repr(ll) == "Node(0)->Node(1)->Node(2)->Node(3)", "Insert Test: Incorrect list representation after inserting at beginning"
    assert ll.size() == 4, "Insert Test: Size should be 4 after inserting at beginning"
    # Insert at end
    node4 = Node(4)
    ll.insert(ll.size(), node4)
    assert repr(ll) == "Node(0)->Node(1)->Node(2)->Node(3)->Node(4)", "Insert Test: Incorrect list representation after inserting at end"
    assert ll.size() == 5, "Insert Test: Size should be 5 after inserting at end"
    print("Insert Test Passed.")

    print("Testing delete (by node)...")
    ll = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    ll.append(node1)
    ll.append(node2)
    ll.append(node3)
    # Delete the middle node.
    ll.delete(node2)
    assert repr(ll) == "Node(1)->Node(3)", "Delete Test: Incorrect list representation after deleting middle node"
    assert ll.size() == 2, "Delete Test: Size should be 2 after deleting middle node"
    # Delete head.
    ll.delete(node1)
    assert repr(ll) == "Node(3)", "Delete Test: Incorrect list representation after deleting head"
    assert ll.size() == 1, "Delete Test: Size should be 1 after deleting head"
    # Delete tail.
    ll.delete(node3)
    assert repr(ll) == "", "Delete Test: List should be empty after deleting tail"
    assert ll.size() == 0, "Delete Test: Size should be 0 after deleting tail"
    print("Delete Test Passed.")

    print("Testing delete_at (by position)...")
    ll = LinkedList()
    nodes = [Node(i) for i in range(5)]  # Create nodes with values 0 to 4
    for node in nodes:
        ll.append(node)
    ll.delete_at(2)  # Deletes node with value 2
    assert repr(ll) == "Node(0)->Node(1)->Node(3)->Node(4)", "Delete_at Test: Incorrect list representation after deleting at position 2"
    assert ll.size() == 4, "Delete_at Test: Size should be 4 after deleting at position 2"
    # Delete head
    ll.delete_at(0)
    assert repr(ll) == "Node(1)->Node(3)->Node(4)", "Delete_at Test: Incorrect list representation after deleting head"
    assert ll.size() == 3, "Delete_at Test: Size should be 3 after deleting head"
    # Delete tail
    ll.delete_at(ll.size() - 1)
    assert repr(ll) == "Node(1)->Node(3)", "Delete_at Test: Incorrect list representation after deleting tail"
    assert ll.size() == 2, "Delete_at Test: Size should be 2 after deleting tail"
    try:
        ll.delete_at(5)
        assert False, "Delete_at Test: Should have raised an IndexError for an out-of-bounds index"
    except IndexError:
        pass
    print("Delete_at Test Passed.")

    print("Testing search...")
    ll = LinkedList()
    node10 = Node(10)
    node20 = Node(20)
    node30 = Node(30)
    ll.append(node10)
    ll.append(node20)
    ll.append(node30)
    result = ll.search(20)
    assert result is not None, "Search Test: Should find node with value 20"
    assert result.value == 20, "Search Test: Found node's value should be 20"
    result_none = ll.search(40)
    assert result_none is None, "Search Test: Should not find a node with value 40"
    print("Search Test Passed.")

    print("Testing size...")
    ll = LinkedList()
    assert ll.size() == 0, "Size Test: Empty list should have size 0"
    node1 = Node(1)
    ll.append(node1)
    assert ll.size() == 1, "Size Test: Size should be 1 after one append"
    node2 = Node(2)
    ll.prepend(node2)
    assert ll.size() == 2, "Size Test: Size should be 2 after prepend"
    ll.delete(node1)
    assert ll.size() == 1, "Size Test: Size should be 1 after deletion"
    print("Size Test Passed.")

    print("All tests passed successfully!")

if __name__ == '__main__':
    run_tests()