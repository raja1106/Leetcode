# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution_Template:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy_head = ListNode(-1,head)
        current = head
        prev = dummy_head
        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return dummy_head.next

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # For printing the list nicely
    def __str__(self):
        result = []
        curr = self
        while curr:
            result.append(str(curr.val))
            curr = curr.next
        return " -> ".join(result)

class Solution_Another_Approach:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode()
        prev = dummy_head
        current = head

        while current:
            if current.val != val:
                prev.next = current
                prev = prev.next
            current = current.next

        prev.next = None  # important to end the list properly
        return dummy_head.next

# Helper to create linked list from list
def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Example Test
sol = Solution()
head = create_linked_list([1, 2, 6, 3, 4, 5, 6])
val_to_remove = 6

print("Original List:")
print(head)

new_head = sol.removeElements(head, val_to_remove)

print("\nList after removing value", val_to_remove, ":")
print(new_head)
