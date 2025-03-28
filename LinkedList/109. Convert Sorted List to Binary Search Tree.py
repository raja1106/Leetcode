class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def find_middle(head):
            slow, fast = head, head
            prev = None  # To keep track of the node before `slow`
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            # Disconnect the left half from the middle
            if prev:
                prev.next = None
            return slow
        # Base case: If the list is empty
        if not head:
            return None

        # Base case: If the list has only one element
        if not head.next:
            return TreeNode(head.val)

        # Step 1: Find the middle element
        mid = find_middle(head)

        # Step 2: The middle element becomes the root
        root = TreeNode(mid.val)

        # Step 3: Recursively build the left and right subtrees
        root.left = self.sortedListToBST(head)  # Left half of the list
        root.right = self.sortedListToBST(mid.next)  # Right half of the list
        return root
