# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swap_pairs_recursive(head: ListNode) -> ListNode: #Space Complexity: O(n) for the recursive call stack.
        # Base case
        if not head or not head.next:
            return head
        # Nodes to be swapped
        first = head
        second = head.next
        # Swap
        first.next = swap_pairs_recursive(second.next)
        second.next = first
        # Return the new head of this swapped pair
        return second

class Solution_More_Intuitive:
    def swapPairs(self, head):
        dummy_head = ListNode(0)
        dummy_head.next = head
        prev = dummy_head

        while head and head.next:
            first_node = head
            second_node = head.next

            # Save the next pair
            next_pair = second_node.next

            # Swap
            prev.next = second_node
            second_node.next = first_node
            first_node.next = next_pair

            # Move pointers forward
            prev = first_node
            head = next_pair

        return dummy_head.next

def swap_pairs(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next and current.next.next:
        first = current.next
        second = current.next.next

        # Perform the swap
        current.next = second
        first.next = second.next
        second.next = first

        # Move to the next pair
        current = first

    return dummy.next
