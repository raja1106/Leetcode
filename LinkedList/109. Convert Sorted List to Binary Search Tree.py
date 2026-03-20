class Solution:#O(nlog(n))
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


class Solution_Optimal_Solution:#O(n)
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        # Step 1: Count nodes to know the index range
        def count_nodes(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count

        n = count_nodes(head)
        self.current = head  # pointer advances during inorder traversal

        def inorder(left, right):
            if left > right:
                return None

            mid = left + (right - left) // 2

            # 1. Recurse LEFT first — this advances self.current to the right spot
            left_child = inorder(left, mid - 1)

            # 2. self.current is now pointing at the correct node for this root
            node = TreeNode(self.current.val)
            self.current = self.current.next  # advance for the next call

            # 3. Recurse RIGHT — self.current continues advancing
            node.left = left_child
            node.right = inorder(mid + 1, right)

            return node

        return inorder(0, n - 1)