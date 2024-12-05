# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Edge case: If the list is empty or has only one node
        if not head or not head.next:
            return head

        # Create a dummy node pointing to the head
        dummy = ListNode(0, head)
        prev = dummy  # `prev` tracks the last distinct node

        current = head
        while current:
            # Check if current node has duplicates
            if current.next and current.val == current.next.val:
                # Skip all nodes with the same value
                while current.next and current.val == current.next.val:
                    current = current.next
                # Link `prev.next` to the node after the duplicates
                prev.next = current.next
            else:
                # Move `prev` to the current node if it's distinct
                prev = current
            # Move `current` to the next node
            current = current.next

        return dummy.next
