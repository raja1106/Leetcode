# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def cycleRemoval(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # No cycle possible; return head as is

        slow = head
        fast = head
        cycle_found = False

        # Detect cycle using two pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle_found = True
                break

        # If no cycle is detected, return the original list
        if not cycle_found:
            return head

        # Find the entry point of the cycle
        start = head
        while start != slow:
            start = start.next
            slow = slow.next

        # Now, to remove the cycle, traverse the cycle until the node whose next is start
        curr = start
        while curr.next != start:
            curr = curr.next
        # Break the cycle
        curr.next = None

        return head
