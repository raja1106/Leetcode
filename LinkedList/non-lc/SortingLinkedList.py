class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # Function to split the linked list into two halves
        def split(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return head, mid

        # Function to merge two sorted linked lists
        def merge(l1, l2):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.value < l2.value:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 if l1 else l2
            return dummy.next

        # Recursively split and merge
        def merge_sort(head):
            if not head or not head.next:
                return head
            left, right = split(head)
            left = merge_sort(left)
            right = merge_sort(right)
            return merge(left, right)

        return merge_sort(head)


# Example usage
# Creating a linked list: 4 -> 2 -> 1 -> 3
node4 = ListNode(3)
node3 = ListNode(1, node4)
node2 = ListNode(2, node3)
head = ListNode(4, node2)

solution = Solution()
sorted_head = solution.sortList(head)

# Printing the sorted linked list
current = sorted_head
while current:
    print(current.value, end=" -> " if current.next else "\n")
    current = current.next
