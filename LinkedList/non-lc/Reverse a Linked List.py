class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the current node's pointer
        prev = current            # Move the prev pointer one step forward
        current = next_node       # Move the current pointer one step forward
    return prev  # prev will be the new head of the reversed list


def reverse_linked_list_using_stack(head):
    if not head:
        return None

    stack = []
    current = head

    # Push all nodes onto the stack
    while current:
        stack.append(current)
        current = current.next

    # Pop nodes from the stack and reconstruct the reversed list
    new_head = stack.pop()
    current = new_head

    while stack:
        current.next = stack.pop()
        current = current.next

    # Set the next of the last node to None
    current.next = None

    return new_head

# Example usage
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

reversed_head = reverse_linked_list(head)

# Printing reversed linked list
current = reversed_head
while current:
    print(current.value, end=" -> " if current.next else "\n")
    current = current.next
