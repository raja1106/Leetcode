# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head):
        dummy_head = ListNode(float("inf"), head)
        prev = dummy_head
        current = head

        while current:
            # If current is the first of a bunch of duplicates, remove them all
            if current.next and current.next.val == current.val:
                next_distinct = current
                while next_distinct and next_distinct.val == current.val:
                    next_distinct = next_distinct.next
                prev.next = next_distinct
                current = next_distinct
            else:
                prev = current # or prev = prev.next
                current = current.next

        return dummy_head.next


class Solution_another_Approach:
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
