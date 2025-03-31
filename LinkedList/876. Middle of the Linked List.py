# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list or single node list
        if not head or not head.next:
            return head

        slow = head
        fast = head

        # Loop condition ensures that in even lists, we stop at the first middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
