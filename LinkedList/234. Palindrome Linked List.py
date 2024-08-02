class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        # Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev, curr = None, slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Compare the first and second half
        first, second = head, prev
        while second:  # Only need to compare until the end of the second half
            if first.value != second.value:
                return False
            first = first.next
            second = second.next

        return True


# Example usage
# Creating a linked list: 1 -> 2 -> 2 -> 1
node4 = ListNode(1)
node3 = ListNode(2, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)

solution = Solution()
print(solution.isPalindrome(head))  # Output: True
