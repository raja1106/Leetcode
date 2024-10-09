class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        queue = collections.deque()
        queue.append(root)
        # or q = collections.deque([root])
        while queue:
            curr_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(curr_level)

        return ans

'''
Understanding Optional[TreeNode]
In Python, type hints are used to indicate the expected type of variables, function parameters, and return values. Optional is a type hint from the typing module, and it is used to indicate that a value can either be of a specified type or None.

Optional[TreeNode]
TreeNode: This is a class representing a node in a binary tree. Each TreeNode typically has a value and references to its left and right children.
Optional[TreeNode]: This means that the value can either be a TreeNode object or None.
So, when you see root: Optional[TreeNode], it means that the root parameter can be either:

An instance of TreeNode (indicating the root node of the tree).
None (indicating that the tree is empty).

'''