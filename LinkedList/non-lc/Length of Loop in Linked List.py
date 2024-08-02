class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def detect_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow  # Cycle detected, return meeting point

    return None  # No cycle detected

def find_cycle_length(meeting_point):
    current = meeting_point
    length = 0

    while True:
        current = current.next
        length += 1
        if current == meeting_point:
            break

    return length

def length_of_cycle(head):
    meeting_point = detect_cycle(head)
    if not meeting_point:
        return 0  # No cycle

    return find_cycle_length(meeting_point)

# Example usage
# Creating a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 5 -> 2 (cycle)
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)
node5.next = node2  # Creating the cycle

cycle_length = length_of_cycle(head)
print(f"The length of the cycle is: {cycle_length}")

# Creating a linked list without a cycle: 1 -> 2 -> 3 -> 4 -> 5
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)

cycle_length = length_of_cycle(head)
print(f"The length of the cycle is: {cycle_length}")
