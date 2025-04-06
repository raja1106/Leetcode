class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: # 2nd Efficient
        def get_length(node):
            i = 0
            curr = node
            while curr:
                curr = curr.next
                i += 1
            return i

        length = get_length(head)
        target_index = length-n
        if target_index == 0:
            return head.next
        i = 1
        prev = head
        current = head.next
        while current:
            if i == target_index:
                prev.next = current.next
                current.next = None
                break
            prev = current
            current = current.next
            i += 1
        return head