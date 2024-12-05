# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return

        # Step 1: Split the list into two halves
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Second half starts after the middle
        second_half = slow.next
        slow.next = None  # Break the list into two halves

        # Step 2: Reverse the second half
        prev, curr = None, second_half
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        second_half = prev  # Reversed second half

        # Step 3: Merge the two halves
        first, second = head, second_half
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
