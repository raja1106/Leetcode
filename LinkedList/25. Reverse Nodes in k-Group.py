class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_list(node):
            prev = None
            current = node

            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return (prev, node)

        if not head or not head.next:
            return head
        dummy_head = ListNode(-1)
        prev_tail = dummy_head
        current = head
        while current:
            current_head = current
            is_size_k = True
            for i in range(k - 1):
                if current:
                    current = current.next
                else:
                    is_size_k = False
            if not is_size_k or current is None:
                prev_tail.next = current_head
            else:
                next_segment = current.next
                current.next = None
                new_head, new_tail = reverse_list(current_head)
                prev_tail.next = new_head
                prev_tail = new_tail
                current = next_segment

        return dummy_head.next