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
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):#Another IK Approach
    def isPalindrome(self, head):
        # If the list is empty or has a single node, it's trivially a palindrome
        if head is None or head.next is None:
            return True

        # Use the slow-fast strategy to find the midpoint
        fast = head
        slow = head
        # Corrected condition to properly handle even-length lists
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the second half of the list
        prev = None
        current = slow.next
        slow.next = None  # Split the list into two parts

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Now 'prev' points to the head of the reversed second half
        is_palindrome = True
        right = prev
        prev = None
        left = head

        # Compare the first half and the reversed second half,
        # while restoring the original order of the second half
        while right:
            if left.val != right.val:
                is_palindrome = False
            left = left.next
            next_node = right.next
            right.next = prev
            prev = right
            right = next_node

        # Reattach the restored second half back to the list
        slow.next = prev
        return is_palindrome


# Example usage
# Creating a linked list: 1 -> 2 -> 2 -> 1
node4 = ListNode(1)
node3 = ListNode(2, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)

solution = Solution()
print(solution.isPalindrome(head))  # Output: True
