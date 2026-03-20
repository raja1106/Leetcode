# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_length(node):
            i = 0
            prev = None
            curr = node
            while curr:
                prev = curr
                curr = curr.next
                i += 1
            return (i, prev)

        list_length, tail_node = get_length(head)

        if list_length == 0:
            return None

        if k % list_length == 0:
            return head

        target_index = list_length - (k % list_length)  # 5-2 = 3

        i = 0
        prev = None
        current = head
        while current:
            if i == target_index:
                prev.next = None
                tail_node.next = head
                return current
            prev = current
            current = current.next
            i += 1

        return head






