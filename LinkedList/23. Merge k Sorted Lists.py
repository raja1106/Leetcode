from typing import List, Optional
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from heapq import heappush, heappop
from typing import List, Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution_Using_Min_heap:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k sorted linked lists into one sorted linked list using a min-heap.
        """
        min_heap = []
        if not lists:
            return None

        # Initialize the heap with the head of each list
        for i, node in enumerate(lists):
            if node:
                heappush(min_heap, (node.val, i, node))

        dummy_head = ListNode()
        current = dummy_head

        # Process the heap until it is empty
        while min_heap:
            val, idx, node = heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heappush(min_heap, (node.next.val, idx, node.next))

        return dummy_head.next


from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution_Using_DivideAndConqure: #Time complexity : O(Nlogk) where k is the number of linked lists.
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        def merge(list1: ListNode, list2: ListNode) -> ListNode:
            dummy = ListNode()
            current = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
            # Attach the remaining nodes
            if list1:
                current.next = list1
            else:
                current.next = list2
            return dummy.next
        def merge_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            if len(lists) == 0:
                return None
            if len(lists) == 1:
                return lists[0]
            if len(lists) == 2:
                return merge(lists[0], lists[1])

            mid = len(lists) // 2
            left = merge_lists(lists[:mid])
            right = merge_lists(lists[mid:])
            return merge(left, right)

        return merge_lists(lists)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:#Time complexity : O(kN) where k is the number of linked lists.


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1, list2):
            temp = ListNode()
            head = temp
            while list1 and list2:
                if list1.val < list2.val:
                    head.next = list1
                    list1 = list1.next
                else:
                    head.next = list2
                    list2 = list2.next
                head = head.next
            while list1:
                head.next = list1
                list1 = list1.next
                head = head.next
            while list2:
                head.next = list2
                list2 = list2.next
                head = head.next
            return temp.next
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        result = lists[0]
        for i in range(1, len(lists)):
            result = merge(result, lists[i])
        return result

