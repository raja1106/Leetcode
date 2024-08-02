class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        # Step 1: Create a new node with the given data
        new_node = Node(data)

        # Step 2: Point the new node to the current head
        new_node.next = self.head

        # Step 3: Update the head pointer to the new node
        self.head = new_node

    def display(self):
        # Function to display the linked list
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

linked_list.display()
