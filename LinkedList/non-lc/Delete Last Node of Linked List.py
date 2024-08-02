class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_last_node(self):
        if self.head is None:
            # If the list is empty
            print("The list is empty, no node to delete.")
            return

        if self.head.next is None:
            # If the list has only one node
            self.head = None
            return

        # Traverse the list to find the second-to-last node
        current = self.head
        while current.next.next:
            current = current.next

        # Update the second-to-last node's next pointer to None
        current.next = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
linked_list = LinkedList()
linked_list.insert_at_head(10)
linked_list.insert_at_head(20)
linked_list.insert_at_head(30)

print("Original list:")
linked_list.display()

linked_list.delete_last_node()

print("List after deleting last node:")
linked_list.display()
