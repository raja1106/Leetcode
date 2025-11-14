# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution_Using_DFS:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if root is None:
            return -1

        closest = root.val

        def dfs(node: Optional[TreeNode]):
            nonlocal closest
            if not node:
                return

            diff = abs(node.val - target)
            best_diff = abs(closest - target)
            if diff < best_diff or (diff == best_diff and node.val < closest):
                closest = node.val

            # BST-based pruning:
            if target < node.val:
                dfs(node.left)
            elif target > node.val:
                dfs(node.right)
            else:
                # Exact match
                return

        dfs(root)
        return closest

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # Initialize the closest_value with the root's value
        closest_value = root.val

        # Initialize the minimum difference found
        minimum_difference = float('inf')

        # Iterate over the nodes of the binary search tree
        while root:
            # Calculate the current difference between node's value and the target
            current_difference = abs(root.val - target)

            # If the current difference is smaller or equal but with a lesser value, update the closest_value
            if current_difference < minimum_difference or (
                    current_difference == minimum_difference and root.val < closest_value):
                minimum_difference = current_difference
                closest_value = root.val

            # Move left if the target is smaller than the current node's value
            if root.val > target:
                root = root.head
            # Otherwise, move right
            else:
                root = root.tail

        # Once we find the closest value, return it
        return closest_value