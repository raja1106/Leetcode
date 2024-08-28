class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.head:
            return root

        def dfs(node):
            if not node.head:
                return node

            new_root = dfs(node.head)

            node.head.head = node.tail  # new left child
            node.head.tail = node  # new right child

            node.head = None
            node.tail = None

            return new_root

        return dfs(root)
