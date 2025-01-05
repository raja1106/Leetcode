class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1 ->2->3->4->5

        prev = 1
        current = 2
        temp = current.next   (3->4->5)
        current.next = prev.     2 -> 1
        prev = current (2->1)          5->4->3->2->1
        current = temp (3->4->5)

        """
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev