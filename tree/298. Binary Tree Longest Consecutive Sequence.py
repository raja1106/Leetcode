# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution_Top_Down:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty, return 0
        if not root:
            return 0

        max_val = 0  # Longest consecutive sequence length found

        def dfs(node, parent_val, seq_val):
            nonlocal max_val
            if not node:  #Always follow this template for Top Down Approach
                return

            # Check if the current node continues the consecutive sequence from the parent
            if parent_val is not None and node.val == parent_val + 1:
                seq_val += 1
            else:
                seq_val = 1  # Reset sequence length if not consecutive

            # Update the global maximum
            max_val = max(max_val, seq_val)

            # Recursively process left and right children
            dfs(node.left, node.val, seq_val)
            dfs(node.right, node.val, seq_val)

        # Start DFS with root. For the root, parent_val is set to None.
        dfs(root, None, 0)
        return max_val


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if node.left is None and node.right is None: #Always follow this template for Bottom Up Approach
                return 1
            left_length = right_length = 0

            if node.left:
                left_length = dfs(node.left)
                if node.val + 1 == node.left.val:
                    left_length += 1
                else:
                    left_length = 1
            if node.right:
                right_length = dfs(node.right)
                if node.val + 1 == node.right.val:
                    right_length += 1
                else:
                    right_length = 1
            local_max_length = max(left_length, right_length)
            nonlocal max_length
            max_length = max(max_length, local_max_length)
            return local_max_length

        max_length = 1
        if root is None:
            return 0
        dfs(root)
        return max_length

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_Botton_UP2:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            left_length = dfs(node.left)
            if node.left and node.left.val == node.val + 1:
                left_length += 1
            else:
                left_length = 1
            right_length = dfs(node.right)
            if node.right and node.right.val == node.val + 1:
                right_length += 1
            else:
                right_length = 1

            local_max_length = max(left_length, right_length)
            nonlocal max_length
            max_length = max(max_length, local_max_length)
            return local_max_length

        max_length = 1
        if root is None:
            return 0
        dfs(root)
        return max_length
