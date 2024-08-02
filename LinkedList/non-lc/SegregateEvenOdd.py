class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def segregateEvenOdd(self, head: ListNode) -> ListNode:
        if not head:
            return None

        even_head = even_tail = None
        odd_head = odd_tail = None
        current = head

        while current:
            next_node = current.next  # Save the next node
            current.next = None  # Break the link to isolate the current node

            if current.value % 2 == 0:
                if not even_head:  # First even node
                    even_head = even_tail = current
                else:
                    even_tail.next = current
                    even_tail = even_tail.next
            else:
                if not odd_head:  # First odd node
                    odd_head = odd_tail = current
                else:
                    odd_tail.next = current
                    odd_tail = odd_tail.next

            current = next_node  # Move to the next node

        if even_tail:
            even_tail.next = odd_head  # Combine even and odd lists
            return even_head
        else:
            return odd_head  # If there are no even nodes, return the odd list

# Example usage
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
node8 = ListNode(8)
node7 = ListNode(7, node8)
node6 = ListNode(6, node7)
node5 = ListNode(5, node6)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)

solution = Solution()
segregated_head = solution.segregateEvenOdd(head)

# Printing the segregated linked list
current = segregated_head
while current:
    print(current.value, end=" -> " if current.next else "\n")
    current = current.next
