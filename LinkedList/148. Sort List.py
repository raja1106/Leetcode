# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeTwoLists(list1, list2):
            dummy = ListNode()
            current = dummy
            while list1 and list2:
                if list1.val <= list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
            if list1:
                current.next = list1
            if list2:
                current.next = list2
            return dummy.next

        if head is None or head.next is None:
            return head
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        right = self.sortList(slow)
        left = self.sortList(head)

        return mergeTwoLists(left, right)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeTwoLists(list1, list2):
            dummy = ListNode()
            current = dummy
            while list1 and list2:
                if list1.val <= list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
            if list1:
                current.next = list1
            if list2:
                current.next = list2
            return dummy.next

        if head is None or head.next is None:
            return head

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        h2 = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(h2)

        return mergeTwoLists(left, right)