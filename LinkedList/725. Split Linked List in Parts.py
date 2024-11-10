# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: ListNode, k: int):
        # Step 1: Count the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Step 2: Determine the base size and extra nodes
        part_size = length // k
        extra = length % k

        # Step 3: Initialize the result array and traverse to split parts
        result = []
        current = head
        for i in range(k):
            part_head = current  # Head of the current part
            size = part_size + (1 if extra > 0 else 0)  # Calculate size of this part
            if extra > 0:
                extra -= 1

            # Traverse to the end of this part
            for j in range(size - 1):
                if current:
                    current = current.next

            # Disconnect the part if it's not empty
            if current:
                next_part = current.next  # Save the next part
                current.next = None  # Break the link
                current = next_part  # Move to the next part

            # Add the part to the result
            result.append(part_head)

        return result
