class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_cycle_start(head):
    if not head or not head.next:
        return None

    slow = head
    fast = head

    # Detect cycle using two pointers
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        # No cycle found
        return None

    # Find the start of the cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

# Example usage
# Creating a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 5 -> 2 (cycle)
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)
node5.next = node2  # Creating the cycle

cycle_start = find_cycle_start(head)
if cycle_start:
    print(f"The cycle starts at node with value: {cycle_start.value}")
else:
    print("No cycle detected.")

# Creating a linked list without a cycle: 1 -> 2 -> 3 -> 4 -> 5
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)

cycle_start = find_cycle_start(head)
if cycle_start:
    print(f"The cycle starts at node with value: {cycle_start.value}")
else:
    print("No cycle detected.")
