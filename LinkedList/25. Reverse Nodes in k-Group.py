class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to reverse k nodes and return the new head and tail
        def reverse_k_nodes(start, k):
            prev, curr = None, start
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            # prev is the new head of the reversed segment, start becomes the new tail
            return prev, start

        # Dummy node to handle edge cases
        dummy_head = ListNode(0)
        dummy_head.next = head
        prev_tail = dummy_head  # This will eventually connect to the new head of each reversed segment

        while head:
            # Check if there are at least k nodes left to reverse
            end = head
            for _ in range(k - 1):
                end = end.next
                if not end:
                    # Fewer than k nodes left, no need to reverse
                    return dummy_head.next

            # Reverse k nodes starting from `head`
            next_segment = end.next
            new_head, new_tail = reverse_k_nodes(head, k)

            # Connect the previous part to the reversed segment
            prev_tail.next = new_head
            new_tail.next = next_segment

            # Move the pointers to the next segment
            prev_tail = new_tail
            head = next_segment

        return dummy_head.next
