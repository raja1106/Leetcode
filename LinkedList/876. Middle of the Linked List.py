# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution_second_Middle:  # 1 2 3 4 5 6 7
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list or single node list
        if not head or not head.next:
            return head

        slow = head
        fast = head

        # Loop condition ensures that in even lists, we stop at the second middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


class Solution_First_Middle:  # 1 2 3 4 5 6 7
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list or single node list
        if not head or not head.next:
            return head

        slow = head
        fast = head

        # Loop condition ensures that in even lists, we stop at the first middle.
        # Because We only jump forward two steps if element is there
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        if fast.next:
            slow = slow.next # for leetcode version to return second middle for even lists

        return slow
