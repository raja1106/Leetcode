# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution_Template:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        curr = head
        index = 1
        prev = dummy_head

        # Move prev and curr to the 'left' position.
        while index < left:
            prev = prev.next
            curr = curr.next
            index += 1

        # Temporarily disconnect the sublist to be reversed.
        prev.next = None
        tail_left = prev
        tail_middle = curr

        # Reverse the sublist from [left, right].
        while index != right + 1:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            index += 1

        # prev now points to the head of the reversed sublist
        head_middle = prev

        # Reconnect the reversed sublist back to the main list.
        tail_middle.next = curr
        prev = tail_left
        prev.next = head_middle

        return dummy_head.next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            tail = None
            current = head
            while current:
                succ = current.next
                current.next = tail  # Reverse the pointer
                tail = current
                current = succ
            return tail

        """
        1. Separate the left part of the list from the given linked list.
        2. Reverse the sublist between left and right.
        3. Reconnect the three parts.
        """
        if left == right or head is None or head.next is None:
            return head

        i = 1
        current = head
        prev = None

        # Move current to the starting point of the sublist (position left)
        while current and i < left:
            prev = current
            current = current.next
            i += 1

        # If prev is not None, break the list
        if prev:
            prev.next = None
        left_tail = prev  # This is the node before the sublist (if any)

        reverse_list_head = current  # Head of the sublist to be reversed
        prev = None

        # Traverse the sublist from position left to right
        while current and i <= right:
            prev = current
            current = current.next
            i += 1

        # Break the sublist at the right end
        if prev:
            prev.next = None
        right_head = current  # Remaining part of the list after the sublist

        # Reverse the sublist
        reversed_segment = reverseList(reverse_list_head)

        # Reconnect the left part to the reversed sublist
        if left_tail:
            left_tail.next = reversed_segment
        else:
            head = reversed_segment  # If left was 1, update head

        # Connect the tail of the reversed sublist to the right part
        reverse_list_head.next = right_head

        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution_Another_Approach:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move prev to the node immediately before the sublist that will be reversed
        for _ in range(left - 1):
            prev = prev.next

        current = prev.next  # The first node in the sublist to reverse

        # Reverse the sublist between left and right in place
        for _ in range(right - left):
            temp = current.next  # Node to be repositioned
            current.next = temp.next  # Remove temp from its current position
            temp.next = prev.next  # Insert temp at the beginning of the reversed sublist
            prev.next = temp  # Update the start of the reversed sublist

        return dummy.next
