class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head  # Return as is if the list has 0 or 1 node

        odd = head
        even = head.next
        evenHead = even  # Save the head of the even group

        while even and even.next:
            odd.next = even.next  # Connect odd to the next odd node
            odd = odd.next  # Move the odd pointer forward
            even.next = odd.next  # Connect even to the next even node
            even = even.next  # Move the even pointer forward

        # Append the even group to the end of the odd group
        odd.next = evenHead
        return head

# Example usage
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)

solution = Solution()
reordered_head = solution.oddEvenList(head)

# Printing the reordered linked list
current = reordered_head
while current:
    print(current.value, end=" -> " if current.next else "\n")
    current = current.next

class Solution_April_2025:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # Edge case: 0 or 1 node

        even_dummy = ListNode()  # Head node of the even-indexed list
        even_tail = even_dummy   # Tail pointer for the even list

        position = 1
        current_node = head
        last_odd = None

        while current_node:
            next_node = current_node.next

            if position % 2 == 0:
                # Move even-indexed node to the even list
                last_odd.next = next_node
                even_tail.next = current_node
                even_tail = even_tail.next
                current_node.next = None  # Detach from original list
            else:
                last_odd = current_node  # Update last odd pointer

            current_node = next_node
            position += 1

        last_odd.next = even_dummy.next  # Append even list to the odd list
        return head

