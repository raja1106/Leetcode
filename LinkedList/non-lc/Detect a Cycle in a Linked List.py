class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False

# Example usage
# Creating a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 5 -> 2 (cycle)
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)
node5.next = node2  # Creating the cycle

print(has_cycle(head))  # Output: True

# Creating a linked list without a cycle: 1 -> 2 -> 3 -> 4 -> 5
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)

print(has_cycle(head))  # Output: False
