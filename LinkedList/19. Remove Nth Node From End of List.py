from typing import Optional


class Solution_Efficient_One_Pass:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy_head (dummy) node whose next pointer is the head
        dummy_head = ListNode(0, head)

        # Step 1: Advance 'leader' n steps ahead
        leader = dummy_head
        for _ in range(n):
            leader = leader.next

        # Step 2: Initialize 'follower' at dummy_head
        # and keep track of the node before it, 'prev'
        follower = dummy_head
        prev = None

        # Step 3: Move 'leader' until it hits the end,
        # simultaneously moving 'follower'
        while leader:
            leader = leader.next
            prev = follower
            follower = follower.next

        # Now 'follower' points to the node to remove
        # 'prev' is the node before it
        prev.next = follower.next

        return dummy_head.next


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