from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = head
        fast = head
        # Detect cycle using two pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                start = head
                while start != slow:
                    start = start.next
                    slow = slow.next
                return start
        return None

class Solution_Extra_memory:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()  # This set will store node references
        current = head
        while current:
            if current in visited:
                return current  # Cycle detected, return the node where the cycle starts
            visited.add(current)
            current = current.next
        return None  # No cycle detected

class Solution_cycleLength:
    def cycleLength(self, head: Optional[ListNode]) -> int:
        if not head or not head.next:
            return 0  # No cycle exists

        slow = head
        fast = head

        # Detect cycle using two pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Cycle detected; now compute its length
                length = 1
                current = slow.next
                while current != slow:
                    length += 1
                    current = current.next
                return length

        return 0  # No cycle detected
