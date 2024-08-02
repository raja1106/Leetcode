class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def reverse(self):
        current = self.head
        temp = None
        while current is not None:
            # Swap the next and prev pointers
            temp = current.prev
            current.prev = current.next
            current.next = temp
            # Move to the next node (which is previous node before swap)
            current = current.prev
        # Update head to the last node processed
        if temp is not None:
            self.head = temp.prev

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# Example usage
dll = DoublyLinkedList()
dll.insert_at_head(10)
dll.insert_at_head(20)
dll.insert_at_tail(30)
print("Original list:")
dll.display()

dll.reverse()
print("Reversed list:")
dll.display()
