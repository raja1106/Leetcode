class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None:
            return None

        # Optional: Validate input values
        if m <= 0 or n < 0:
            raise ValueError("m must be > 0 and n must be >= 0")

        current = head

        # Iterate over the entire linked list
        while current:
            # Skip m - 1 nodes (retain these nodes)
            for _ in range(m - 1):
                if current is None:
                    break
                current = current.next

            # If we reach the end of the list, return the head as no more nodes need to be deleted
            if current is None:
                return head

            # Now current is the m-th node, set to_delete to the next node
            to_delete = current.next

            # Skip n nodes to delete them
            for _ in range(n):
                if to_delete is None:
                    break
                to_delete = to_delete.next

            # Link the m-th node to the node after the last deleted node
            current.next = to_delete

            # Move to the next group
            current = to_delete

        return head
