from heapq import heappush, heappop
from typing import List, Optional


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __lt__(self, other):
        return self.value < other.value


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        min_heap = []

        # Initialize the heap with the head of each list
        for l in lists:
            if l:
                heappush(min_heap, l)

        dummy = ListNode()
        current = dummy

        while min_heap:
            # Get the smallest node
            smallest_node = heappop(min_heap)
            current.next = smallest_node
            current = current.next

            # If there's a next node, push it into the heap
            if smallest_node.next:
                heappush(min_heap, smallest_node.next)

        return dummy.next


# Example usage
# Creating linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, 2 -> 6
l1 = ListNode(1, ListNode(4, ListNode(5)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
l3 = ListNode(2, ListNode(6))
lists = [l1, l2, l3]

solution = Solution()
merged_head = solution.mergeKLists(lists)

# Printing the merged linked list
current = merged_head
while current:
    print(current.value, end=" -> " if current.next else "\n")
    current = current.next
