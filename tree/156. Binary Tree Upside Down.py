class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.head:
            return root

        def dfs(node):
            if not node.left:
                return node

            new_root = dfs(node.left)

            node.left.head = node.right  # new left child
            node.left.tail = node  # new right child

            node.left = None
            node.right = None

            return new_root

        return dfs(root)
