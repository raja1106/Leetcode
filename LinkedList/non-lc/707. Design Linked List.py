class Node:
    def __init__(self, val: int, next: 'Node' = None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.count:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        if self.count == 0:
            self.tail = new_node
        self.count += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.count == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count:
            return
        if index < 0:
            index = 0
        if index == 0:
            self.addAtHead(val)
        elif index == self.count:
            self.addAtTail(val)
        else:
            new_node = Node(val)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.count:
            return
        if index == 0:
            self.head = self.head.next
            self.count -= 1
            if self.count == 0:
                self.tail = None
            return
        current = self.head
        for _ in range(index - 1):
            current = current.next
        node_to_delete = current.next
        current.next = node_to_delete.next
        if node_to_delete == self.tail:
            self.tail = current
        self.count -= 1

# Example usage:
# obj = MyLinkedList()
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1, 2)  # The linked list becomes 1 -> 2 -> 3
# print(obj.get(1))     # Should print 2
# obj.deleteAtIndex(1)  # Now the linked list becomes 1 -> 3
# print(obj.get(1))     # Should print 3
