# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
                root = root.left
            # Otherwise, move right
            else:
                root = root.right

        # Once we find the closest value, return it
        return closest_value