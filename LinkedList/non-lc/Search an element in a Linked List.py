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

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

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

key = 20
found = linked_list.search(key)
if found:
    print(f"Element {key} is present in the linked list.")
else:
    print(f"Element {key} is not present in the linked list.")

key = 40
found = linked_list.search(key)
if found:
    print(f"Element {key} is present in the linked list.")
else:
    print(f"Element {key} is not present in the linked list.")
