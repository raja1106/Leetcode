# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution_June_2025:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        dummy_node = ListNode()
        current = head
        prev = dummy_node
        while current:

            for _ in range(m): # 0 1
                prev.next = current #dummy->11
                prev = prev.next
                if current:
                    current = current.next
                else:
                    return dummy_node.next
            #end of for loop 3
            prev.next = None

            for _ in range(n): # 0 1 2
                if current:
                    current = current.next # 4 5 6
                else:
                    return dummy_node.next
        return  dummy_node.next
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
