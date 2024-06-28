class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        queue = collections.deque([root])

        def is_palindrom(level_list):
            i = 0
            j = len(level_list) - 1
            while i < j:
                if level_list[i] != level_list[j]:
                    return False
                i += 1
                j -= 1
            return True
        while queue:
            level_size = len(queue)
            level_list = []

            for i in range(level_size):
                node = queue.popleft()
                if not node:
                    level_list.append(None)
                    continue
                level_list.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            if not is_palindrom(level_list):
                return False
        return True

    def isSymmetric_DFS(self, root: TreeNode) -> bool:
        def is_mirror(node1: TreeNode, node2: TreeNode) -> bool:

            # Both nodes are None, meaning both subtrees are empty, thus symmetric
            if node1 is None and node2 is None:
                return True
            # If only one of the nodes is None or if the values don't match, the subtrees aren't mirrors
            if node1 is None or node2 is None or node1.val != node2.val:
                return False
            # Check the outer and inner pairs of subtrees
            return is_mirror(node1.left, node2.right) and is_mirror(node1.right, node2.left)

        # Start the recursion with root as both parameters, as the check is for the tree with itself
        return is_mirror(root, root)
