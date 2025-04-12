class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]):
        if not head:
            return head
        dummy_head = ListNode(float('-inf'),head)
        prev = dummy_head
        current = head
        while current:
            if current.val == prev.val: #removing node
                prev.next = current.next
                current = current.next
            else: # doing work for your sub-ordinate
                prev = current
                current = current.next
        return dummy_head.next
